from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Trending, Details, Cast, Video
from .serializers import (
    TrendingSerializer,
    DetailsSerializer,
    CastSerializer,
    VideoSerializer,
)
import requests
import logging
import os

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TrendingViewSet(viewsets.ModelViewSet):
    queryset = Trending.objects.all().order_by("tv_id")
    serializer_class = TrendingSerializer
    pagination_class = PageNumberPagination

    @action(detail=False, methods=["get"])
    def fetch(self, request):
        count = 100
        per_page = 20

        headers = {
            "accept": "application/json",
            "Authorization": os.getenv("AUTHORIZATION_TOKEN"),
        }

        all_trending_data = []

        for page in range(1, (count // per_page) + 2):
            trending_url = f"https://api.themoviedb.org/3/trending/tv/day?language=zh-TW&page={page}"
            trending_response = requests.get(trending_url, headers=headers)

            if trending_response.status_code == 200:
                trending_data = trending_response.json().get("results", [])
                all_trending_data.extend(trending_data)
                if len(all_trending_data) >= count:
                    break
            else:
                return Response(
                    {"status": "error", "message": "Failed to fetch data"},
                    status=trending_response.status_code,
                )

        all_trending_data = all_trending_data[:count]

        for trending_item in all_trending_data:
            # 儲存 trending 資料
            trending_obj, _ = Trending.objects.update_or_create(
                tv_id=trending_item["id"],
                defaults={
                    "backdrop_path": f"https://image.tmdb.org/t/p/w500{trending_item['backdrop_path']}",
                    "name": trending_item["name"],
                    "overview": trending_item["overview"],
                    "poster_path": f"https://image.tmdb.org/t/p/w500{trending_item['poster_path']}",
                    "adult": trending_item["adult"],
                },
            )

            # 呼叫 details API
            details_url = (
                f"https://api.themoviedb.org/3/tv/{trending_obj.tv_id}?language=zh-TW"
            )
            details_response = requests.get(details_url, headers=headers)
            if details_response.status_code == 200:
                details_data = details_response.json()
                Details.objects.update_or_create(
                    tv_id=trending_obj,
                    defaults={
                        "last_episode_name": (
                            details_data["last_episode_to_air"]["name"]
                            if details_data.get("last_episode_to_air")
                            else None
                        ),
                        "genres": ",".join(
                            [genre["name"] for genre in details_data["genres"]]
                        ),
                    },
                )

            # 呼叫 casts API
            casts_url = f"https://api.themoviedb.org/3/tv/{trending_obj.tv_id}/aggregate_credits?language=zh-TW"
            casts_response = requests.get(casts_url, headers=headers)
            if casts_response.status_code == 200:
                casts_data = casts_response.json().get("cast", [])
                Cast.objects.update_or_create(
                    tv_id=trending_obj,
                    defaults={
                        "cast_names": ", ".join([cast["name"] for cast in casts_data]),
                    },
                )

            # 呼叫 videos API
            if details_data["languages"] and details_data["origin_country"]:
                language_param = f"{details_data['languages'][0]}-{details_data['origin_country'][0]}"
            else:
                language_param = "en-US"

            videos_url = f"https://api.themoviedb.org/3/tv/{trending_obj.tv_id}/videos?language={language_param}"
            videos_response = requests.get(videos_url, headers=headers)
            if videos_response.status_code == 200:
                videos_data = videos_response.json().get("results", [])
                youtube_video = next(
                    (video for video in videos_data if video["site"] == "YouTube"),
                    None,
                )
                if youtube_video:
                    Video.objects.update_or_create(
                        tv_id=trending_obj,
                        defaults={
                            "name": youtube_video["name"],
                            "url": f"http://youtube.com/watch?v={youtube_video['key']}",
                        },
                    )

        return Response(
            {
                "status": "success",
                "message": "Trending data fetched and stored successfully.",
            },
            status=status.HTTP_201_CREATED,
        )


class DetailsViewSet(viewsets.ModelViewSet):
    queryset = Details.objects.all().order_by("tv_id")
    serializer_class = DetailsSerializer
    pagination_class = PageNumberPagination


class CastViewSet(viewsets.ModelViewSet):
    queryset = Cast.objects.all().order_by("tv_id")
    serializer_class = CastSerializer
    pagination_class = PageNumberPagination


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all().order_by("tv_id")
    serializer_class = VideoSerializer
    pagination_class = PageNumberPagination

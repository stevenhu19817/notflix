document.addEventListener('DOMContentLoaded', function () {
    var customSelect = document.querySelector('.custom-select');
    var selectSelected = customSelect.querySelector('.select-selected');
    var selectItems = customSelect.querySelector('.select-items');

    selectSelected.addEventListener('click', function (e) {
        e.stopPropagation();
        this.classList.toggle('active');
        this.classList.toggle('select-arrow-active');
        selectItems.classList.toggle('select-hide');
    });

    var selectOptions = selectItems.getElementsByClassName('select-item');
    for (var i = 0; i < selectOptions.length; i++) {
        selectOptions[i].addEventListener('click', function (e) {
            var selectedText = this.textContent;
            selectSelected.querySelector('span').textContent = selectedText;

            // 更新選中項的樣式
            var current = selectItems.querySelector('.selected');
            if (current) current.classList.remove('selected');
            this.classList.add('selected');

            selectItems.classList.add('select-hide');
            selectSelected.classList.remove('select-arrow-active');
        });
    }

    document.addEventListener('click', function () {
        selectItems.classList.add('select-hide');
        selectSelected.classList.remove('select-arrow-active');
        selectSelected.classList.remove('active');
    });
});
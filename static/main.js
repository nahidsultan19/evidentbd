document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('#btn').onclick = () => {
        let values = document.querySelector('input').value;
        alert(`Result: ${values}`);

    }
});
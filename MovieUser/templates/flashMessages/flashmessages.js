
{% if messages %}
    document.addEventListener("DOMContentLoaded", function(event) {
        toastr.options = { "closeButton": true, "debug": false, "newestOnTop": false,
            "progressBar": true, "positionClass": "toast-top-right", "preventDuplicates": false,
            "onclick": null, "showDuration": "300", "hideDuration": "1000", "timeOut": "5000",
            "extendedTimeOut": "1000", "showEasing": "swing", "hideEasing": "linear",
            "showMethod": "fadeIn", "hideMethod": "fadeOut" };
        {% autoescape off %}
            {% for msg in messages %}
                toastr.{{ msg.level_tag }}("{{ msg }}");
            {% endfor %}
        {% endautoescape %}
    });
{% endif %}
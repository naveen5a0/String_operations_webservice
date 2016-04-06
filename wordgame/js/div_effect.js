$(document).ready(function() {
    $("#history_div").hide();
    $("#advance_div").hide();
    var $default_check = $('input:radio[name=math_group]');
    $default_check.filter('[value=word]').prop('checked', true)
    $("input[name$='math_group']").click(function() {
        var test = $(this).val();

        
        if(test=="word")
        {
            $("#history_div").hide();
            $("#word_div").show();
            $("#advance_div").hide();

        }
        else if(test=="history")
        {
            $("#history_div").show();
            $("#word_div").hide();
            $("#advance_div").hide();

        }
        else if(test=="advance")
        {
            $("#history_div").hide();
            $("#word_div").hide();
            $("#advance_div").show();

        }


    });
});
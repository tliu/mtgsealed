$ = jQuery
$ ->
    $("#num-boosters").focus()
    $("#num-boosters").keypress (e) ->
        if e.which == 13
            count = $("#num-boosters").val()
            $.get "http://127.0.0.1:5000/boosters?count=#{count}", (data) ->
                data = data.replace("{","").replace("}","").replace(/"/g,"").split(", ")
                for s in data
                    console.log s.split(":")
                






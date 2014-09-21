$ = jQuery
$ ->
    $("#num-boosters").focus()
    $("#num-boosters").keypress (e) ->
        if e.which == 13
            count = $("#num-boosters").val()
            $.get "http://127.0.0.1:5000/boosters?count=#{count}", (data) ->
                data = data.replace("{","").replace("}","").replace(/"/g,"").split(", ")
                for s in data
                    p = s.split(":")
                    id = p[0]
                    c = p[1]
                    console.log "out: " + id + ", " + c
                    add_card = do(c) -> (data) =>
                        console.log data
                        data = data.replace(/^\s+|\s+$/g, "").replace(/]/g, "").replace(/"/g,"").split(",")
                        data[3] = data[3][1]
                        console.log "card-block-#{data[3]}"
                        if data[3] is "W"
                            color = "#F0F5B8"
                        if data[3] is "U"
                            color = "#2aa9f7"
                        if data[3] is "B"
                            color = "#999999"
                        if data[3] is "R"
                            color = "#fc3f3f"
                        if data[3] is "G"
                            color = "#17bd45"
                        if data[3] is "M"
                            color = "#ffd700"
                        if data[3] is "L"
                            color = "#f4a460"
                        if data[3] is "A"
                            color = "#964B00"
                        $("#card-block-#{data[3]}").append("<div class=\"card\" style=\"margin-top: 6px;border: 1px solid #555; border-radius: 5px; padding: 4px; background-color: #{color};\">
                            <span style=\"font-size: 18px; margin-right: 6px\">#{c}</span> <b>#{data[1]}</b>
                        </div>")

                    $.get "http://127.0.0.1:5000/cards/id/#{id}", add_card


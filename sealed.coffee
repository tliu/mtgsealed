$ = jQuery
$ ->
    console.log "foo"
    console.log $("#cards")
    $.ajax
    $("#cards").autocomplete source: ['test', 'foo']
    
    console.log "foo"





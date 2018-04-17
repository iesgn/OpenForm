$(document).ready(function() {
    var max_fields      = 10; //maximum input boxes allowed
    var wrapper         = $(".instances_form"); //Fields wrapper
    var add_button      = $(".add_instance"); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function(e){ //on add input button click
        e.preventDefault();
        if(x < max_fields){ //max input box allowed
            x++; //text box increment
            // $(wrapper).append('<div><input type="text" placeholder="Instance Name" name="instance_name' + x + '" /><input type="text" placeholder="Image ID" name="instance_image_id' + x + '" /><input type="text" placeholder="Favlor ID" name="instance_flavor_id' + x + '" /><input type="text" placeholder="Key pair name" name="instance_key_pair' + x + '" /><input type="text" placeholder="Security groups" name="instance_security_groups' + x + '" /><a href="#" class="remove_instance">X</a></div>'); //add input box
            $(wrapper).append('<div><input type="text" placeholder="Instance Name" name="instance_name" required/><input type="text" placeholder="Image ID" name="instance_image_id" /><input type="text" placeholder="Favlor ID" name="instance_flavor_id" /><input type="text" placeholder="Key pair name" name="instance_key_pair" /><input type="text" placeholder="Security groups" name="instance_security_groups" /><a href="#" class="remove_instance">X</a></div>');
        }
    });

    $(wrapper).on("click",".remove_instance", function(e){ //user click on remove text
        e.preventDefault(); $(this).parent('div').remove(); x--;
    })
});
$(document).ready(function() {
    var max_fields      = 5; //maximum input boxes allowed
    var wrapper         = $(".networks_form"); //Fields wrapper
    var add_button      = $(".add_network"); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function(e){ //on add input button click
        e.preventDefault();
        if(x < max_fields){ //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div><input type="text" placeholder="Network Name" name="network_name" required/><input type="text" placeholder="IP range" name="network_cidr" required/><a href="#" class="remove_network">X</a></div>');
        }
    });

    $(wrapper).on("click",".remove_network", function(e){ //user click on remove text
        e.preventDefault(); $(this).parent('div').remove(); x--;
    })
});
$(document).ready(function() {
    var max_fields      = 5; //maximum input boxes allowed
    var wrapper         = $(".volumes_form"); //Fields wrapper
    var add_button      = $(".add_volume"); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function(e){ //on add input button click
        e.preventDefault();
        if(x < max_fields){ //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div><input type="text" placeholder="Volume Name" name="volume_name" required/><input type="text" placeholder="Volume size" name="volume_size" required/><input type="text" placeholder="Volume description" name="volume_desc" required/><a href="#" class="remove_volume">X</a></div>');
        }
    });

    $(wrapper).on("click",".remove_volume", function(e){ //user click on remove text
        e.preventDefault(); $(this).parent('div').remove(); x--;
    })
});
// $(document).ready(function(){
//   var global_image = $("input[name=global_image_text]")
//   var images = $("input[name=instance_image_id]")
//   var apply_button = $(".global_image")
//
//   $(apply_button).click(function(){
//     $(images).val($(global_image).val());
//   });
// });

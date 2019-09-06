$( document ).ready(function(){
    mosp.init();
});

var mosp = {

    formElements        : [
        {
            id          : "form-starYear",
            name        : "starYear",
            type        : "number",
            classDiv    : "mt-2",
            icon 		: "fa fa-calendar",
            required    : false,
            minChar     : 4,
            maxChar     : 4,
            msg         : {
                placeholder       : "Start year",
                error             : "Must contain 4 characters"
            }
        },
        {
            id          : "form-endYear",
            name        : "endYear",
            type        : "number",
            classDiv    : "mt-2",
            icon 		: "fa fa-calendar",
            required    : false,
            minChar     : 4,
            maxChar     : 4,
            msg         : {
                placeholder       : "End year",
                error             : "Must contain 4 characters"
            }
        },
        {
            id          : "form-starMonth",
            name        : "startMonth",
            type        : "number",
            classDiv    : "mt-4",
            icon 		: "fa fa-calendar",
            required    : false,
            minChar     : 1,
            maxChar     : 2,
            msg         : {
                placeholder       : "Start month",
                error             : "Must contain at least 1 character and 2 maximum"
            }
        },
        {
            id          : "form-endMonth",
            name        : "endMonth",
            type        : "number",
            classDiv    : "mt-2",
            icon 		: "fa fa-calendar",
            required    : false,
            minChar     : 1,
            maxChar     : 2,
            msg         : {
                placeholder       : "End month",
                error             : "Must contain at least 1 character and 2 maximum"
            }
        }
    ],

    formLib             : null,

    init: function() {

		mosp.formLib = validateFormLib(mosp.formElements, function(result){
        });  

        $( document ).keyup(function(e){
            if (e.keyCode == 13){
                mosp.validateForm();
            }
        });

        $("#btn-calc").click(function(){
            mosp.validateForm();
        });

    },

    validateForm        : function () {
        mosp.formLib.validateForm(function (pData) {
            if (pData.status == CONSTANS.OK){
                mosp.getPassiveRateAvg(pData.data);
            }
        });
    },

    getPassiveRateAvg: function(pData) {
        f_globals.resource('GET', "/getPassiveRateAvg" , pData,
            function(response) {
            	if (response.value){
                    try{
                        $("#calc-result").text(response.value.toFixed(2));
                    }catch{
                        $("#calc-result").text("Invalid parameters");
                    }
            	}
            },
            function(error) {
                $("#calc-result").text("Start the backend and wait for a moment");
            }
        );
    }
};

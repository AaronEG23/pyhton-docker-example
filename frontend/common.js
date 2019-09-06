var CONSTANS    = {
    OK              : 100,
    ERROR           : 200,
};

var f_globals   = { 

    endPoint            : "http://127.0.0.1:5000",      

    resource: function(type, url, params, callback, error, upload) {
        urlRequest = f_globals.endPoint + url;
        console.log(urlRequest);
        console.log(JSON.stringify(params))
        $.ajax({
            dataType: 'json',
            contentType: 'application/json',
            method: type,
            url: urlRequest,
            data: type == 'GET' ? params : JSON.stringify(params),
            timeout: upload ? 240000 : 10000,
            success: function(response, status) {
                console.log(response);
                if (callback) callback(response);
                
            },
            error: function(xhr, status, err) {
                if (error) error(err, status);
            }
        });
    }

};

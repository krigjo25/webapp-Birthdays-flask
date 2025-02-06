document.addEventListener('DOMContentLoaded', function() {

    const sendData = {
        'id': '',
        'name':'',
        'bday':'',
        'btn_name':'',
        'updated_name':'',
        'updated_bday':''
    }
    function TransferData(arg)
    {
        //  Transfer to Flask
        
        $.ajax({
            url: 'http://127.0.0.1:5000/',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(arg),
            success: function(response){console.log(response)},
            error: function(error) { console.log('ERROR : ', error);}
        });
        return;
    }

    function contentHandler(btn)
    {
        const column = document.querySelectorAll('[contenteditable]');

        for(let i = 0; i < column.length; i+=2)
        {
            if (column[i].isContentEditable)
            {
                if (column[i].attributes[1].value == btn)
                {
                    sendData["updated_name"] = column[i].textContent;
                    sendData["updated_bday"] = column[i+1].textContent;
                }
            }
        }
        return;
    }

    function main()
    {
        //  Initializing variables
        const btn = document.querySelectorAll('.edit');

        for (let i=0; i < btn.length; i++)
        {
            btn[i].addEventListener('click', (e) => {
                //e.preventDefault();

                sendData['btn_name'] = btn[i].name;
                sendData['id'] = btn[i].value
                //  Handle the editablecontent
                contentHandler(btn[i].value);

                // Transfer adata to Flask
                TransferData(sendData);
            });
        }

        return;
    }

    main();
});

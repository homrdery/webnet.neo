function getform () {
        $('#Form').load('/getform.html?action=subAddr', function(responseTxt, statusTxt, jqXHR)
            {
                if(statusTxt == 'success'){
                        $('#addForm').modal();
                    }
                    if(statusTxt == 'error'){
                        alert('Error: ' + jqXHR.status + ' ' + jqXHR.statusText);
                    }
                }
        );
    };

function deladdr( e, dt, node, config )  {
        var id = $('#myTable').DataTable.$('tr.selected')[0].id;
        console.log('Выбран пользователь под id ='+id);
        $("#Form").load("/getform.html?action=delAddr&id="+id, function(responseTxt, statusTxt, jqXHR)
        {
            if(statusTxt == 'success'){
                    $('#addFormdel').modal();
                }
                if(statusTxt == 'error'){
                    alert('Error: ' + jqXHR.status + ' ' + jqXHR.statusText);

                }
        });

}

function tableinit () {
    var table = $('#myTable').DataTable({
    dom: 'Bfrtip',
    buttons: [
        {
            text:      '<i class="fa fa-plus"></i>',
            attr:  {
                title: 'Add item',
                id: 'BtAdd'
                },
            titleAttr: 'Add item',
            action: function ( e, dt, node, config ) {
                alert( 'Button activated' );
                }
        },
        {
            text:      '<i class="fa fa-pen"></i>',
            attr:  {
                title: 'Edit item',
                id: 'BtEdit'
                },
            init: function ( dt, node, config ) {
                this.disable();
            },
            action: function readdr( e, dt, node, config )  {
                var id = $('#myTable').DataTable.$('tr.selected')[0].id;
                console.log('re make user id ='+mac_addr);
                $("#Form").load("/getform.html?action=reAddr&id="+mac_addr, function(responseTxt, statusTxt, jqXHR)
                {
                    if(statusTxt == 'success'){
                            $('#addFormdel').modal();
                        }
                        if(statusTxt == 'error'){
                            alert('Error: ' + jqXHR.status + ' ' + jqXHR.statusText);

                        }
                });

            }
        },
        {
            text:      '<i class="fas fa-trash  aria-hidden="true"></i>',
            attr:  {
                title: 'Delete item',
                id: 'BtDelete'
            },

            init: function ( dt, node, config ) {
                this.disable();
            },
            action:    deladdr

        }
    ],
    pageLength: 25,
    select: true,
    rowId: 'id',
    language: {
        url:"/static/datatables/ru.json"
        },
});
    table.on( 'select deselect', function () {
        var selectedRows = table.rows( { selected: true } ).count();
        table.buttons(['#BtEdit']).enable( selectedRows === 1 );
        table.buttons(['#BtDelete']).enable( selectedRows > 0 );
    });
}

$(tableinit);



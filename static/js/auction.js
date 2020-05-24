






 

$('.main_cards').on('click', '.btn', function() {
	var elementId = $(this).data('id');
	console.log(elementId)

	var serializedData = $("#add_form_" + elementId).serialize();
	console.log(serializedData)

	$.ajax({
		url: $("#add_form_" + elementId).data('url'),
		data: serializedData,
		type: 'post',
		success: function(response){
			console.log(response.bid_data.new_bid)
			$('#bid_list_'  + elementId).append('<small>bid: ' + response.bid_data.bid + ' | </small>');
			if (response.bid_data.new_bid != undefined) {
				console.log($(this))
				$('#actual_price_val_'  + elementId).replaceWith($('#actual_price_val_'  + elementId).text('actual price: ' + response.bid_data.new_bid))
			};

		}
	})

	$('#add_form_' + elementId)[0].reset();
	
});




// var csrfJqToken = $('input[name=csrfmiddlewaretoken]').val();


//     console.log('csrfJqToken', csrfJqToken)

// function BidButtonClickHandler(event){

// 	event.preventDefault()

//     const form = event.target.form

//     const token = form.querySelector('input').value
//     const bid = form.querySelector('#id_bid').value
//     const auctionId = form.querySelector('#id_auction').value
//     const buyerId = form.querySelector('#id_buyer_id').value
//     // // const getPath = form.querySelector('#id_buyer_id').value
//     // const csrfToken = form.getELementsByName('csrfmiddlewaretoken')

//     // console.log('csrfToken', csrfToken)
//     console.log(form)
//     console.log(token)

//     const path = "/"


// // csrfmiddlewaretoken=DlhBFzzzEHMBXl6wugLhptiCIsBLiRM6zvNF80d8S4CELSM466j66xbZlXJ04leR&bid=145&auction=17&buyer_id=9

// 	const jsonStr = 'csrfmiddlewaretoken=' + csrfJqToken + '&bid=' + bid + '&auction=' + auctionId + '&buyer_id=' + buyerId

//     console.log('jsonStr', jsonStr)

//     const auction = {
//     	csrfmiddlewaretoken: csrfJqToken,
//     	bid: bid,
//     	auction: auctionId,
//     	buyer_id: buyerId,
//     }


//     const xhr = new XMLHttpRequest()

//     const json = JSON.stringify({

//     	csrfmiddlewaretoken: csrfJqToken,
//     	bid: bid,
//     	auction: auctionId,
//     	buyer_id: buyerId,
//     	})

//     console.log('json', json)
//     xhr.open('POST', path)
//     xhr.setRequestHeader('Content-type', 'application/json; charset=utf-8');

//     xhr.send(jsonStr)

// }

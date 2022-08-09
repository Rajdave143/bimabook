(function($){
	var submit;
	$('#tblList').DataTable({
		"dom": "<'row'<'col-sm-12 col-md-6'l><'col-sm-12 col-md-6'f>>\n  <'table-responsive'tr>\n <'row align-items-center'<'col-sm-12 col-md-5'i><'col-sm-12 col-md-7 d-flex justify-content-end'p>>",
		"language": {
		  paginate: {
			previous: '<i class="fa fa-lg fa-angle-left"></i>',
			next: '<i class="fa fa-lg fa-angle-right"></i>'
		  }
		},
		"bLengthChange": true,
		"autoWidth" : true,
		"statesave": true,
		"columnDefs": [
			{targets: [0,2],className: "text-center w-10pc"},
			{targets: [3],className: "text-center w-10pc nowrap",orderable: false},
		],
	});
	$('form[name="frmvc"]').ajaxForm({
		beforeSend: function() {
			var form=$('form[name="frmvc"]');
			if(!(form).parsley().isValid()){return false;}
			submit=form.find("button[type='submit']");
			btnBusy(submit);
		},
		url:"Submit",
		data: {request: 'NewVC'},
		success: function(html, statusText, xhr, $form) {		
			try{
				obj = $.parseJSON(html);	
				toastr[obj.status](obj.response);
				if((obj.status)=='success'){	
					if($("#vncckreload").is(":checked")){
						$form[0].reset();$("#vncckreload").attr('checked','checked');
					}else{
						window.location.reload();
					}
				}
			}
			catch (e){
				systemError();
			}
			btnFree(submit);
		}
	});	
	$('form[name="frmvcedit"]').ajaxForm({
		url:"Submit",
		data: {request: 'EditVC'},
		success: function(html, statusText, xhr, $form) {		
			try{
				obj = $.parseJSON(html);
				toastr[obj.status](obj.response);				
				if((obj.status)=='success'){	
					setTimeout(function(){$('#mdlvehiclecategoryedit').modal('hide');window.location.reload();}, 2000);
				}
			}
			catch (e){
				systemError();
			}
		}
	});
	$("#vc_remove").click(function() {
		$.post("Submit", {request:'RemoveVC',id:$("#vcrid").val()}, function(data) {
			try{
				obj = $.parseJSON(data);
				toastr[obj.status](obj.response);
				if((obj.status)=='success'){	
					$("a.selected").closest('tr').remove();
					$('#mdlvehiclecategorydel').modal('hide');
				}
			}
			catch (e){
				systemError();
			}
		});
	});
	
	//Models
	$('#tblModelsList').DataTable({
		"dom": "<'row'<'col-sm-12 col-md-6'l><'col-sm-12 col-md-6'f>>\n  <'table-responsive'tr>\n        <'row align-items-center'<'col-sm-12 col-md-5'i><'col-sm-12 col-md-7 d-flex justify-content-end'p>>",
		"language": {
		  paginate: {
			previous: '<i class="fa fa-lg fa-angle-left"></i>',
			next: '<i class="fa fa-lg fa-angle-right"></i>'
		  }
		},
		"bLengthChange": true,
		"autoWidth" : true,
		"statesave": true,
		"columnDefs": [
			{targets: [0,3],className: "text-center w-10pc"},
			{targets: [4],className: "text-center nowrap",orderable: false},
		],
	});
	$('form[name="frmvm"]').ajaxForm({
		beforeSend: function() {
			var form=$('form[name="frmvm"]');
			if(!(form).parsley().isValid()){return false;}
			submit=form.find("button[type='submit']");
			btnBusy(submit);
		},
		url:"Submit",
		data: {request: 'NewVM'},
		success: function(html, statusText, xhr, $form) {		
			try{
				obj = $.parseJSON(html);	
				toastr[obj.status](obj.response);
				if((obj.status)=='success'){	
					if($("#vnmckreload").is(":checked")){
						$form[0].reset();$("#vnmckreload").attr('checked','checked');
					}else{
						window.location.reload();
					}
				}
			}
			catch (e){
				systemError();
			}
			btnFree(submit);
		}
	});	
	$('form[name="frmvmedit"]').ajaxForm({
		url:"Submit",
		data: {request: 'EditVM'},
		success: function(html, statusText, xhr, $form) {		
			try{
				obj = $.parseJSON(html);
				toastr[obj.status](obj.response);				
				if((obj.status)=='success'){	
					setTimeout(function(){$('#mdlvehiclecategoryedit').modal('hide');window.location.reload();}, 2000);
				}
			}
			catch (e){
				systemError();
			}
		}
	});
	$("#vm_remove").click(function() {
		$.post("Submit", {request:'RemoveVM',id:$("#vmrid").val()}, function(data) {
			try{
				obj = $.parseJSON(data);
				toastr[obj.status](obj.response);
				if((obj.status)=='success'){	
					$("a.selected").closest('tr').remove();
					$('#mdlvehiclemodeldel').modal('hide');
				}
			}
			catch (e){
				systemError();
			}
		});
	});
	
	//Automobiles Company
	$('#tblMakeby').DataTable({
		"dom": "<'row'<'col-sm-12 col-md-6'l><'col-sm-12 col-md-6'f>>\n  <'table-responsive'tr>\n        <'row align-items-center'<'col-sm-12 col-md-5'i><'col-sm-12 col-md-7 d-flex justify-content-end'p>>",
		"language": {
		  paginate: {
			previous: '<i class="fa fa-lg fa-angle-left"></i>',
			next: '<i class="fa fa-lg fa-angle-right"></i>'
		  }
		},
		"bLengthChange": true,
		"autoWidth" : true,
		"statesave": true,
		"columnDefs": [
			{targets: [0,2],className: "text-center w-10pc nowrap"},
			{targets: [3],className: "text-center nowrap w-10pc",orderable: false},
		],
	});
	$('form[name="frmmb"]').ajaxForm({
		beforeSend: function() {
			var form=$('form[name="frmmb"]');
			if(!(form).parsley().isValid()){return false;}
			submit=form.find("button[type='submit']");
			btnBusy(submit);
		},
		url:"Submit",
		data: {request: 'NewMB'},
		success: function(html, statusText, xhr, $form) {		
			try{
				obj = $.parseJSON(html);	
				toastr[obj.status](obj.response);
				if((obj.status)=='success'){	
					if($("#mbckreload").is(":checked")){
						$form[0].reset();$("#mbckreload").attr('checked','checked');
					}else{
						window.location.reload();
					}
				}
			}
			catch (e){
				systemError();
			}
			btnFree(submit);
		}
	});	
	$('form[name="frmmbedit"]').ajaxForm({
		url:"Submit",
		data: {request: 'EditMB'},
		success: function(html, statusText, xhr, $form) {		
			try{
				obj = $.parseJSON(html);
				toastr[obj.status](obj.response);				
				if((obj.status)=='success'){	
					setTimeout(function(){$('#mdlvehiclemakebyedit').modal('hide');window.location.reload();}, 2000);
				}
			}
			catch (e){
				systemError();
			}
		}
	});
	$("#mb_remove").click(function() {
		$.post("Submit", {request:'RemoveMB',id:$("#mbrid").val()}, function(data) {
			try{
				obj = $.parseJSON(data);
				toastr[obj.status](obj.response);
				if((obj.status)=='success'){	
					$("a.selected").closest('tr').remove();
					$('#mdlvehiclemakebydel').modal('hide');
				}
			}
			catch (e){
				systemError();
			}
		});
	});
	
})(jQuery);
function update(src){
	var id=$(src).data('id');
	var c=$(src).parent().parent('tr').find("td:eq(1)").text();
	var s=$(src).parent().parent('tr').find("td:eq(2)").text();
	$("#category").val(c);$("#vcid").val(id);
	$("#status_update").val(s);
	$('#mdlvehiclecategoryedit').modal('show');
}
function remove(src){
	var id=$(src).data('id');
	$("#vcrid").val(id);
	$('#mdlvehiclecategorydel').modal('show');
	$('a.selected').removeClass('selected');
	$(src).addClass('selected');
}	
function updateVM(src){
	var id=$(src).data('id');
	var m=$(src).parent().parent('tr').find("td:eq(1)").text();
	var c=$(src).parent().parent('tr').find("td:eq(2)").text();
	var s=$(src).parent().parent('tr').find("td:eq(3)").text();
	$("#model").val(m);$("#vmid").val(id);
	$("#vehicle_makeby").val(c);
	$("#vmstatus_update").val(s);
	$('#mdlvehiclemodeledit').modal('show');
}
function removeVM(src){
	var id=$(src).data('id');
	$("#vmrid").val(id);
	$('#mdlvehiclemodeldel').modal('show');
	$('a.selected').removeClass('selected');
	$(src).addClass('selected');
}
function updateMB(src){
	var id=$(src).data('id');
	var c=$(src).parent().parent('tr').find("td:eq(1)").text();
	var s=$(src).parent().parent('tr').find("td:eq(2)").text();
	$("#makeby").val(c);$("#mbid").val(id);
	$("#mbstatus_update").val(s);
	$('#mdlvehiclemakebyedit').modal('show');
}
function removeMB(src){
	var id=$(src).data('id');
	$("#mbrid").val(id);
	$('#mdlvehiclemakebydel').modal('show');
	$('a.selected').removeClass('selected');
	$(src).addClass('selected');
}	
$(document).ready(function() {
    // events
    $("#analysis").click(function(event) {
        event.preventDefault();

        console.log('use button')

        if($("#checkAnalysis").val() == "on") {
            if($("#context").val() == "") {
                $("#context").focus();
            } else {
                $("#checkAnalysis").val("off");
                stopWordList = getStopWordList();
                analysis(stopWordList);
            }

        }


    });

    $("#inputFileAnalysis").click(function(event) {
        event.preventDefault();

        console.log('use button')

        if($("#checkFile").val() == "on") {
            if($("#inputFile").val() == "") {
            } else {
                $("#checkFile").val("off");
                stopWordList = getStopWordList();
                fileUpload(stopWordList);
            }

        }


    });


    $("#addStopWord").click(function(event) {
        event.preventDefault();

        console.log('add btn');
        addStopWord();

    });

    $("#delStopWord").click(function(event) {
        event.preventDefault();

        console.log('del btn');
        delStopWord();

    });

    $("#viewChart").click(function(event) {
        event.preventDefault();

        if($("#div_chart").css("display") == "none"){
            createChart();
            $("#div_chart").show();
        } else {
            $("#div_chart").hide();
        }

    });

    $("#viewCloud").click(function(event) {
        event.preventDefault();

        if($("#div_cloud").css("display") == "none"){

            $("#div_cloud").show();
        } else {
            $("#div_cloud").hide();
        }

    });

    $("#useFile").click(function(event) {
        event.preventDefault();

        $("#div_useText").hide();
        $("#div_useFile").show();
    });

    $("#useText").click(function(event) {
        event.preventDefault();

        $("#div_useText").show();
        $("#div_useFile").hide();
    });

    $("#inputFile").on('change',function() {

		let ext = $(this).val().split('.').pop().toLowerCase();
		$("#inputFileLabel").text($("#inputFile").val().split('\\').pop());

		if ($.inArray(ext, [ 'txt' ]) == -1) {
			$("#fileInputMsg").html("<span class='text-danger'>파일타입을 확인해주세요</span>");
			$("#checkFile").val("off");
		} else {
			$("#fileInputMsg").html("<span class='text-success'>사용할 수 있습니다.</span>");
			$("#checkFile").val("on");
		}

	});




    // functions
    function analysis(stopWordList, context) {

        context = (typeof context !== 'undefined') ? context : $("#context").val();

        var data = {
            "type"         : "nounCount",
            "context"      : context,
            "stopWordList" : stopWordList,
            "countKeyWord" : $("#countKeyWord").val()
        };

        jQuery.ajaxSettings.traditional = true;

        $.ajax({
            type        : "post",
            url         : "analysis/",
            data        : data,
            dataType    : 'json',
            success     : function(res) {
                console.log('ajax success')
                $("#checkAnalysis").val("on");
                $("#div_chart").hide();
                showKeyword(res);
                $("#output").show();
            },
            error       : function(xhr) {
                console.log('ajax failed');
                console.log(xhr);
                $("#checkAnalysis").val("on");
                $("#div_chart").hide();
            }


        })

    }


    function fileUpload(stopWordList) {

        console.log('file upload')

        jQuery.ajaxSettings.traditional = true;
        var files = $("#inputFile").prop("files");
        var data = {
            "files" : files
        }

        console.log(data)

        if(files.length > 0) {
            $.ajax({
                type      : "post",
                url       : "fileUpload/",
                data      : data,
                dataType  : 'json',
                success   : function(res) {
                    console.log('success file upload');
                    analysis(stopWordList, res.context);

                },
                error     : function(xhr) {
                    console.log('failed file upload');
                    console.log(xhr);

                }
            })
        }




    }


    function showKeyword(input) {
        var wordList = input['dictList'];
        var cloudPath = input['cloudPath'];

        $("#img_cloud").empty();
        $("#div_cloud").hide();

        showImg(cloudPath);

        var div_outputKey = $("#outputKeyword");
        var strDOM = "";

        var tableBody = $("#datatable_body");
        var table_strDOM = "";

        div_outputKey.empty();
        tableBody.empty();


        for(var idx=0, tup; tup=wordList[idx]; idx++) {
            // listAdded
            strDOM += '<input type="text" style="width:100%" readonly value="'+ tup[0] + '(' + tup[1]+')' +'"/>'

            // tableAdded
            table_strDOM += "<tr>"
            table_strDOM += "<th>" + tup[0] + "</th>"
            table_strDOM += "<td>" + tup[1] + "</td>"
            table_strDOM += "</tr>"

        }
        div_outputKey.append(strDOM);
        tableBody.append(table_strDOM);


    }

    function addStopWord() {
        var strDOM = '<input type="text" style="width:100%;" placeholder="불용어입력"/>';
        var div_stopWord = $("#div_stopWord");

        div_stopWord.append(strDOM);
    }

    function delStopWord() {
        var div_stopWord = $("#div_stopWord");

        var childCount = div_stopWord.children().length;
        if(childCount > 1) {
            var last_child = div_stopWord.children(":last");
            last_child.remove();
        }

    }

    function getStopWordList() {
        var div_stopWord = $("#div_stopWord")
        var childCount = div_stopWord.children().length;

        var stopWords = [];

        var tmp = div_stopWord.children(":first")
        for(var idx=0; idx < childCount; idx++) {
            if(tmp.val() != "") {
                stopWords.push(tmp.val());
            }
            if(idx != (childCount-1)) {
                tmp = tmp.next();
            }

        }

        return stopWords.join('^');

    }

    function showImg(cloudPath) {
        img_cloud = $("#img_cloud");
        img_cloud.empty();

        strDOM = ""
        strDOM += '<img src="' + cloudPath + '" style="width:1000px">'

        console.log(cloudPath);

        img_cloud.append(strDOM);

    }



    function createChart() {
        Highcharts.chart('container', {
            data: {
                table: 'datatable'
            },
            chart: {
                type: 'column'
            },
            title: {
                text: '키워드 별 카운트 수'
            },
            label: {
                enabled: false,
            },
            credits: {
                enabled: false,
            },
            legend: {
                enabled: false,
            },
            xAxis: {
                title: {
                  text: '키워드'
                }
            },
            yAxis: {
                allowDecimals: false,
                title: {
                  text: '카운트 수'
                }
            },
            tooltip: {
                formatter: function() {
                  return '<b>' + this.series.name + '</b><br/>' +
                    this.point.y + ' ' + this.point.name.toLowerCase();
                }
            }
        });

    }




})
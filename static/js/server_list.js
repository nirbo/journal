$(document).ready(function() {
    var $serverTable = $("#server-table");

    $serverTable.on("click", "tbody tr", function() {
        $this = $(this);
        $row_id = $this.find("td.id").html();
        // console.log($row_id);
    });
});


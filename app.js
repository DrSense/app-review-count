$(document).ready(function () {
    $("#searchBtn").click(function () {
        var appName = $("#appName").val();
        var platform = $("#platform").val();
        var timeFilter = $("#timeFilter").val();

        if (appName.trim() !== "") {
            // Make an AJAX request to the backend
            $.ajax({
                type: "POST",
                url: "/get_reviews",
                data: { app_name: appName, platform: platform, time_filter: timeFilter },
                success: function (response) {
                    displayReviews(response.reviews);
                },
                error: function (error) {
                    console.log("Error:", error);
                }
            });
        }
    });

    function displayReviews(reviews) {
        var reviewsList = $("#reviewsList");
        reviewsList.empty();

        reviews.forEach(function (review) {
            var stack = $("<div class='reviewStack'>");
            stack.append("<p><strong>Review Name:</strong> " + review.review_name + "</p>");
            stack.append("<p><strong>Date of Review:</strong> " + review.review_date + "</p>");
            stack.append("<p><strong>Review:</strong> " + review.review_content + "</p>");
            stack.append("<p><strong>Date Imported:</strong> " + review.import_date + "</p>");

            stack.click(function () {
                displaySelectedReview(review);
            });

            reviewsList.append(stack);
        });
    }

    function displaySelectedReview(review) {
        var selectedReview = $("#selectedReview");
        selectedReview.empty();

        selectedReview.append("<p><strong>Source:</strong> " + review.platform + "</p>");
        selectedReview.append("<p><strong>Date of Review (Range):</strong> " + review.review_date_range + "</p>");
        selectedReview.append("<p><strong>Date of Import:</strong> " + review.import_date + "</p>");
        selectedReview.append("<p><strong>Review Content:</strong> " + review.review_content + "</p>");
    }
});

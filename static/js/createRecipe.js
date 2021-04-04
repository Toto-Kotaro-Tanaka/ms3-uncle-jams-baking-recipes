/*jshint esversion: 6 */

// Credit: Sanwebe @ https://www.sanwebe.com/2013/03/addremove-input-fields-dynamically-with-jquery
$(document).ready(function () {
    // Ingredients Fields
    let maxIngredsFields = 15;
    let ingredsWrapper = $(".input-fields-wrap-ingreds");
    let ingredsAddButton = $(".btn-add-field-ingreds");

    let ingreds = 1;
    $(ingredsAddButton).click(function (e) {
        e.preventDefault();
        if (ingreds < maxIngredsFields) {
            ingreds++;
            $(ingredsWrapper).append(
                '<div><input type="text" name="recipe_ingreds" class="form-control bg-color-49332-06" maxlength="50" required /><a class="remove-field-ingreds color-fbeade"><i class="fas fa-trash-alt"></i></a></div>'
            );
        }
    });

    $(ingredsWrapper).on("click", ".remove-field-ingreds", function (e) {
        e.preventDefault();
        $(this).parent("div").remove();
        ingreds--;
    });

    // Steps Fields
    let maxStepsFields = 10;
    let stepsWrapper = $(".input-fields-wrap-steps");
    let stepsAddButton = $(".btn-add-field-steps");

    let steps = 1;
    $(stepsAddButton).click(function (e) {
        e.preventDefault();
        if (steps < maxStepsFields) {
            steps++;
            $(stepsWrapper).append(
                '<div><textarea name="recipe_steps" class="form-control bg-color-49332-06" rows="3" maxlength="300" required></textarea><a class="remove-field-steps color-fbeade"><i class="fas fa-trash-alt"></i></a></div>'
            );
        }
    });

    $(stepsWrapper).on("click", ".remove-field-steps", function (e) {
        e.preventDefault();
        $(this).parent("div").remove();
        steps--;
    });
});
// -- /End of Credit --

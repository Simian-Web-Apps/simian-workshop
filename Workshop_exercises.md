# Exercises

* Each section of the workshop contains:
  * The goal of the section
  * References to the section(s) of the  Simian GUI documentation <https://doc.simiansuite.com/simian-gui/index.html> that are relevant. Note that it contains a search option.
  * A description of what needs to be done.
  * Items marked `Optional` are not part of the main flow of the workshop, but are worth looking into.

* Note that the fully functional web app that we are working towards is available as the `simian.examples.workshop_example` module. If you are stuck, you may find the solution there.
* Note that the Simian GUI documentation contains examples for both Python and MATLAB. Per code block the used language is shown with an icon in the upper right corner.
* Note that during this workshop we only cover a part of Simian GUI. If you are a bit quicker than the others, you can try out some additional properties and methods of the components that we are adding and see how they affect your web app.


## Running workshop web app

Goal: Assert that you can run the web app locally, so that you can see the effects of the changes to the form that you are going to make later on.

<https://doc.simiansuite.com/simian-gui/introduction/python.html#local-use>

* Run the `workshop_application.py` module as a script to view the current status of the `workshop_application.py` web app.
* You should see an web app that only contains the text "Intentionally left empty".
* Close the window
  

## Change a label

Goal: Assert that you are editing the correct file and that changes to the form definition can be viewed immediately.

<https://doc.simiansuite.com/simian-gui/initialization/htmlelement.html>  
<https://doc.simiansuite.com/simian-gui/initialization/navbar.html>

* In the `workshop_application` module edit the "Intentionally left empty" text in the `gui_init` function.
* Run the `workshop_application.py` file again to see the effect of your changes.
* Change the text again, but this time click the refresh button in the top-right of the app.

Optional:

* The navigation bar's contents can also be modified.


## Add a Load button

Goal: Learn how to add a component to the web app and make the it 'functional'.

<https://doc.simiansuite.com/simian-gui/initialization/button.html>  
<https://doc.simiansuite.com/simian-gui/events/guiEvent.html>

* Add a `Button` to the form by calling its constructor in the `gui_init` function.
* Give it a `LoadData` event.
* Click the button. A message should be shown at the top of the web app.
* Put a breakpoint in the `gui_event` function. Click the button again, to trigger debugging at the breakpoint.

Optional:

* Use your IDE's tab-completion on the Button object to view its attributes and see the docstrings and type hints.
* Add an icon to the button. Available are the Font-Awesome 4.7.0 icons. <https://fontawesome.com/v4/icons/>
* To debug the front-end in the browser set the `debug` option to True in the `Uiformio` call.


## Add a DataTables table

Goal: Add a `DataTables` table to the web app.

<https://doc.simiansuite.com/simian-gui/initialization/datatables.html>

* Use the Python code example from the documentation as a starting point. Refresh the web app to have a look.
* Remove the `defaultValue` and modify the `DataTables`' columns to prepare for showing the values from the `GAP_DATA` (pandas DataFrame) constant in the `workshop_application.py` module.
  `table_column_names = list(GAP_DATA.columns)` gives you a list with the column headers.
* (We will use this code later on, so do not remove it.)


## Use .json file web app definition

Goal: learn about adding components without writing code.

<https://doc.simiansuite.com/simian-gui/initialization/structure.html#adding-components-from-json>

* Replace the enabled Form construction call in `gui_init` with the out-commented one.
* Refresh the app
* Inspect the `workshop_application.json` file.


## Load a definition into Simian Builder

Goal: Learn to open Simian Builder.

<https://doc.simiansuite.com/simian-gui/builder.html>

* Open a new Terminal / Console in your IDE and start Simian Builder in a separate Python process with the command:
  python -m simian.builder
* Click the `Load ...` button
  * Replace the `Workspace folder` content with the folder containing the workshop files.
  * In the `Module name` field put: `workshop_application`
  * Click the `Load JSON` button. The Builder should have loaded the definition in the .json file. It should only show a label.

Optional:

* Click the `Open new Builder` button.
* In the new Builder window, click the `New` button and create a new web app next to the workshop app.


## Add a component in Simian Builder

Goal: Learn to use Simian Builder.

* Add a DataTables table to the app by dragging the `DataTables` item from the `Data` list into the app. Note that the DataTables has less Builder options compared to other components.
* The `API` tab's `Property Name` field sets the `key` of the component. The key is needed to access the component and its values in the backend.
* Click the `Save` button to save the `DataTables` definition into the `workshop_application.json` file.
* Click the `Preview` button or refresh the web app.

Optional:

* Go through the lists of components in the Builder to get an overview of what is available.
* Try the `Search field(s)` option above the lists to more easily find the component you want.
* Drag a TextField component into the builder and go through the tabs to get an overview of the options.


## Use code with a component from the Builder

Goal: Learn how to modify/set properties of a component that was added with the builder.

<https://doc.simiansuite.com/simian-gui/initialization/structure.html#initialization-code>

* Use the code from the other `DataTables` object in an initialize function to modify the new DataTables component.
* Add a `Form.componentInitializer` line to the `gui_init` function and register the initialize function.
* Test your code by refreshing your app.
* Remove the old DataTables component.


## Show GAP_DATA on load event

Goal: Modify the submission data during an event and show data in the web app.

<https://doc.simiansuite.com/simian-gui/events/guiEvent.html>  
<https://doc.simiansuite.com/simian-gui/events/submission.html>

* Remove any defaultValue of the `DataTables` table.
* In the `LoadData` event modify the submission data so that the `GAP_DATA` is put in the `DataTables` table. The `DataTables` table should contain 1,704 rows.
* Note the table's default search option, pagination and column sorting.
  
Optional:

* Refer to the `DataTables` component documentation for further possibilities.


## Alternative event routing

Goal: Route events more easily using event dispatching.

<https://doc.simiansuite.com/simian-gui/events/guiEvent.html#registering-events-explicitly>

* Move data load functionality to a dedicated `load_data` function
* Route the event to the `load_data` function by registering it and using dispatching. (The `addAlert` in the else may be removed or put in an `except ImportError:` block.) Test the web app.


## Add a Plotly figure

Goal: Add a `Plotly` component to the form and fill it during an event to visualize data.

<https://doc.simiansuite.com/simian-gui/initialization/plotly.html#python>

* Add an empty `Plotly` figure to the form in `gui_init` or the builder.
* Give it a 'key': `plot`
* Fill the `Plotly` figure during the `LoadData` event by using the prepared `update_plot` function in your `workshop_application.py` file.

Refer to the Plotly documentation for all possibilities:

<https://plotly.com/python/line-and-scatter/>  
<https://plotly.com/python-api-reference/generated/plotly.express.scatter.html>


## Change layout

Goal: Modify the layout of the web app.

<https://doc.simiansuite.com/simian-gui/initialization/nesting.html>
<https://doc.simiansuite.com/simian-gui/initialization/columns.html>


* Add a `Columns` component to the form.
* Put the `DataTables` table in one column and the `Plotly` component in the other.

Optional:

* Play with the number and widths of the columns to see the effect.
* What happens when you make the web app window narrow?


## Year(s) filtering

Goal: Adding a `Select` component and filling it with non-hardcoded options.

<https://doc.simiansuite.com/simian-gui/initialization/select.html>
<https://doc.simiansuite.com/simian-gui/how_to/update_selectboxes.html>

* Add a `Select` component
* Add a `Hidden` components with key `availableYears`.
* During the `LoadData` event fill the Hidden component with the `GAP_DATA` years via the submission data. You can get the unique years with:
    `gap_years = sorted(set(GAP_DATA["year"]))`
* Make the `Select` control depend on the `Hidden` control by setting the `Data Source Type` to `Custom` and the `Custom values` to:
  `values = data.availableYears`
* During the load event select one year in the Years `Select` control via the submission data. Note that the other years must remain selectable.

Optional:

* What happens when you type in the `Select` component?
* Set the property `multiple` of the Select component to True. What happens?
* Repeat for selecting continents. (Note that in the `filter_data` function `isin()` outputs can be combined with an `&` operator.)
    `& GAP_DATA["continent"].isin(...)`


## Number of Years

Goal: Add a `Number` component and fill it client-side with the number of selected years.

<https://doc.simiansuite.com/simian-gui/initialization/component.html>

* Add a disabled `Number` component with label "Number of selected years"
* Use the `setCalculateValue` method with inputs `"value = data.<Year Select key>.length"` and False.
  
(Optional):

* Make the `Number` component enabled and see what the `allowCalculateOverride` property is for.


## Validate a setting

Goal: Add a `Number` control and add client-side validation.

<https://doc.simiansuite.com/simian-gui/initialization/properties/validate.html>

* Add a `Number` control to allow entering a year number.
* Create a `Validate` object with custom validation. The parent is the `Number` control.
`"valid = data.availableYears.includes(input);"`
* Add a custom error message.
* Test: What happens when an invalid year is entered?

Optional:

* Set a `placeholder` "yyyy" and/or `defaultValue` on the `Number` component.
* Set the load data Button's `disableOnInvalid` property to True.
  * What happens now when an invalid year is entered?
  * Alternatively, set the load data `Button`'s `showValidations` property to True.


## Filter table and plot data

Goal: reduce the data being shown.

* Use the prepared `filter_data` function in your workshop_application.py module to filter the data shown in the table and plot.
* The Years `Select` control has one year selected, so we expect to only see those items in the table and plot.


## Filter after selection change

Goal: Filter data when year selection is changed in the web app by the user.

<https://doc.simiansuite.com/simian-gui/advanced_features/value_changed_event.html>  
<https://doc.simiansuite.com/simian-gui/initialization/structure.html#initialization-code>


* Set Year Select control to be `triggerHappy` with a custom event name.
* Register the event in `gui_event` to reapply the filters when the Year selection changes.
* What happens when no years are selected?

Note that for components where the user types a new value the `triggerHappy` option can result in many events being sent to the back-end. For these components you:

* need to set a debounce time: <https://doc.simiansuite.com/simian-gui/advanced_features/value_changed_event.html#debouncing> 
* or only want an event when the user stops editing and leaves the component: <https://doc.simiansuite.com/simian-gui/advanced_features/focus_lost_event.html>.


## Scenarios EditGrid

Goal: Add an `EditGrid` component and show information in it.

<https://doc.simiansuite.com/simian-gui/initialization/editgrid.html>

Note that the `getSubmissionData` and `setSubmissionData` functions only work on the complete `EditGrid`.

* Create a "Scenarios" `EditGrid`
* Drag the existing year selection `Number` control into the EditGrid to have an instance in each row of the EditGrid.
* Add a disabled `Number` control to the `EditGrid`.
* Set `tableView` property to True for the `Number` controls to ensure they are shown when the row is collapsed.

* Add a Scenario run Button (outside the EditGrid!) and add an event
  * In the event function, loop over the rows in the EditGrid and put the total population for the selected year in the second `Number` control.
    `float(new_gap["pop"].sum())`
  * Note that non-saved values are not available in the back end when the run button is clicked.

Optional:

* Add labels to the controls in the `EditGrid` when they do not yet have any, as these are used as column headers.
* Temporarily make existing Year `Number` control `triggerHappy`. What happens?
* Replace the `EditGrid` with a `DataGrid`.
  

## Optional steps

* Add `Tabs` and `Columns` to change the layout of the web app.
* Hide year and continent `Select` controls when no data is loaded yet.
  <https://doc.simiansuite.com/simian-gui/how_to/conditional_hide.html>
  `show = data.availableYears.length != 0`
* Alternatively, disable the year and continent `Select` controls when no data is loaded yet.
  For this use the Component class' `disableWhen` method or the `Logic` tab in the Builder.


## (Optional) Deploy the Python code

Goal: Make the Simian web app available on the deployment environment.

<https://doc.simiansuite.com/simian-gui/deployment/python.html>

* Setup your deployment environment as documented.
* Follow the documented steps to install Simian in the deployment environment.
* Modify the documented, deployment target specific Python code to connect the deployment environment with your web app.
* Deploy your web app and connection code to the deployment environment.

Optional:

* Test the deployed web app by sending a POST request (as documented) and verify that you get a successful response with a `session_id`.


## (Optional) Configure the portal

Goal: Make the deployed Simian web app available from the portal.

<https://doc.simiansuite.com/simian-portal/user_guide/save-load-configurations.html>  
<https://doc.simiansuite.com/simian-portal/user_guide/edit-configuration.html>

* Go to the admin portal where you want to make the web app accessible.
* Click 'Add configuration' button and fill in the form.
  * In the `cURL options` panel specify where your deployed Simian web app can be reached.
* Reload the user portal and click the web app you just added. If everything was setup correctly, you should see your Simian web app in your browser.

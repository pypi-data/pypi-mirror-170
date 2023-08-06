"use strict";
(self["webpackChunk_jupyterlab_scheduler"] = self["webpackChunk_jupyterlab_scheduler"] || []).push([["lib_components_job-row_js-lib_index_js-lib_mainviews_list-jobs_js-lib_notebook-jobs-panel_js"],{

/***/ "./lib/advanced-options.js":
/*!*********************************!*\
  !*** ./lib/advanced-options.js ***!
  \*********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _mui_material__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @mui/material */ "webpack/sharing/consume/default/@mui/material/@mui/material");
/* harmony import */ var _mui_material__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_mui_material__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _components_cluster__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./components/cluster */ "./lib/components/cluster.js");
/* harmony import */ var _components_icon_buttons__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./components/icon-buttons */ "./lib/components/icon-buttons.js");
/* harmony import */ var _hooks__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./hooks */ "./lib/hooks.js");





const AdvancedOptions = (props) => {
    var _a;
    const formPrefix = 'jp-create-job-advanced-';
    const trans = (0,_hooks__WEBPACK_IMPORTED_MODULE_2__.useTranslator)('jupyterlab');
    const handleInputChange = (e) => props.handleModelChange(Object.assign(Object.assign({}, props.model), { [e.target.name]: e.target.value }));
    const handleTagChange = (event) => {
        var _a;
        if (props.jobsView !== 'CreateJob') {
            return; // Read-only mode
        }
        const { name, value } = event.target;
        const tagIdxMatch = name.match(/^tag-(\d+)$/);
        if (tagIdxMatch === null) {
            return null;
        }
        const newTags = (_a = props.model.tags) !== null && _a !== void 0 ? _a : [];
        newTags[parseInt(tagIdxMatch[1])] = value;
        props.handleModelChange(Object.assign(Object.assign({}, props.model), { tags: newTags }));
    };
    const addTag = () => {
        var _a;
        const newTags = [...((_a = props.model.tags) !== null && _a !== void 0 ? _a : []), ''];
        props.handleModelChange(Object.assign(Object.assign({}, props.model), { tags: newTags }));
    };
    const deleteTag = (idx) => {
        var _a;
        const newTags = (_a = props.model.tags) !== null && _a !== void 0 ? _a : [];
        newTags.splice(idx, 1);
        props.handleModelChange(Object.assign(Object.assign({}, props.model), { tags: newTags }));
    };
    const tags = (_a = props.model.tags) !== null && _a !== void 0 ? _a : [];
    const createTags = () => {
        return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_1__.Stack, { spacing: 2 },
            tags.map((tag, idx) => (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_components_cluster__WEBPACK_IMPORTED_MODULE_3__.Cluster, { key: idx, justifyContent: "flex-start" },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_1__.TextField, { label: trans.__('Tag %1', idx + 1), id: `${formPrefix}tag-${idx}`, name: `tag-${idx}`, value: tag, onChange: handleTagChange }),
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_components_icon_buttons__WEBPACK_IMPORTED_MODULE_4__.DeleteButton, { onClick: () => {
                        // Remove tag
                        deleteTag(idx);
                        return false;
                    }, title: trans.__('Delete tag %1', idx + 1), addedStyle: { marginTop: '4px' } })))),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_components_cluster__WEBPACK_IMPORTED_MODULE_3__.Cluster, { justifyContent: "flex-start" },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_components_icon_buttons__WEBPACK_IMPORTED_MODULE_4__.AddButton, { onClick: (e) => {
                        addTag();
                        return false;
                    }, title: trans.__('Add new tag') }))));
    };
    const showTags = () => {
        if (!props.model.tags) {
            return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_1__.Stack, { spacing: 2 },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("p", null,
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement("em", null, trans.__('No tags')))));
        }
        return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_1__.Stack, { spacing: 2 }, tags.map((tag, idx) => (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_1__.TextField, { label: trans.__('Tag %1', idx + 1), id: `${formPrefix}tag-${idx}`, name: `tag-${idx}`, value: tag, InputProps: {
                readOnly: true
            } })))));
    };
    // Tags look different when they're for display or for editing.
    const tagsDisplay = props.jobsView === 'CreateJob' ? createTags() : showTags();
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_1__.Stack, { spacing: 4 },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_1__.TextField, { label: trans.__('Idempotency token'), variant: "outlined", onChange: handleInputChange, value: props.model.idempotencyToken, id: `${formPrefix}idempotencyToken`, name: "idempotencyToken", InputProps: { readOnly: props.jobsView !== 'CreateJob' } }),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_1__.FormLabel, { component: "legend" }, trans.__('Tags')),
        tagsDisplay));
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (AdvancedOptions);


/***/ }),

/***/ "./lib/components/cluster.js":
/*!***********************************!*\
  !*** ./lib/components/cluster.js ***!
  \***********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "Cluster": () => (/* binding */ Cluster)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);

function Cluster(props) {
    let cls = 'jp-jobs-Cluster';
    cls += ` justify-content-${props.justifyContent || 'flex-start'}`;
    cls += ` align-items-${props.alignItems || 'center'}`;
    cls += ` gap-${props.gap || 1}`;
    return react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: cls }, props.children);
}


/***/ }),

/***/ "./lib/components/compute-type-picker.js":
/*!***********************************************!*\
  !*** ./lib/components/compute-type-picker.js ***!
  \***********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "ComputeTypePicker": () => (/* binding */ ComputeTypePicker)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _mui_material__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @mui/material */ "webpack/sharing/consume/default/@mui/material/@mui/material");
/* harmony import */ var _mui_material__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_mui_material__WEBPACK_IMPORTED_MODULE_1__);


function ComputeTypePicker(props) {
    const environmentObj = props.environmentList.find(env => env.name === props.environment);
    if (!environmentObj || !environmentObj.compute_types) {
        return null;
    }
    const computeTypes = environmentObj.compute_types;
    const labelId = `${props.id}-label`;
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement((react__WEBPACK_IMPORTED_MODULE_0___default().Fragment), null,
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_1__.InputLabel, { id: labelId }, props.label),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_1__.Select, { labelId: labelId, name: props.name, id: props.id, onChange: props.onChange, value: props.value }, computeTypes.map((ct, idx) => (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_1__.MenuItem, { value: ct, key: idx }, ct))))));
}


/***/ }),

/***/ "./lib/components/environment-picker.js":
/*!**********************************************!*\
  !*** ./lib/components/environment-picker.js ***!
  \**********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "EnvironmentPicker": () => (/* binding */ EnvironmentPicker)
/* harmony export */ });
/* harmony import */ var _mui_material__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @mui/material */ "webpack/sharing/consume/default/@mui/material/@mui/material");
/* harmony import */ var _mui_material__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_mui_material__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _hooks__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../hooks */ "./lib/hooks.js");



function EnvironmentPicker(props) {
    const trans = (0,_hooks__WEBPACK_IMPORTED_MODULE_2__.useTranslator)('jupyterlab');
    if (props.environmentList.length === 0) {
        return react__WEBPACK_IMPORTED_MODULE_1___default().createElement("em", null, trans.__('Loading …'));
    }
    const labelId = `${props.id}-label`;
    return (react__WEBPACK_IMPORTED_MODULE_1___default().createElement((react__WEBPACK_IMPORTED_MODULE_1___default().Fragment), null,
        react__WEBPACK_IMPORTED_MODULE_1___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_0__.InputLabel, { id: labelId }, props.label),
        react__WEBPACK_IMPORTED_MODULE_1___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_0__.Select, { labelId: labelId, name: props.name, id: props.id, onChange: props.onChange, value: props.initialValue }, props.environmentList.map((env, idx) => (react__WEBPACK_IMPORTED_MODULE_1___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_0__.MenuItem, { value: env.label, title: env.description, key: idx }, env.name))))));
}


/***/ }),

/***/ "./lib/components/heading.js":
/*!***********************************!*\
  !*** ./lib/components/heading.js ***!
  \***********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "Heading": () => (/* binding */ Heading)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);

function Heading(props) {
    switch (props.level) {
        case 1:
            return react__WEBPACK_IMPORTED_MODULE_0___default().createElement("h1", { className: "jp-jobs-Heading" }, props.children);
        case 2:
            return react__WEBPACK_IMPORTED_MODULE_0___default().createElement("h2", { className: "jp-jobs-Heading" }, props.children);
        case 3:
            return react__WEBPACK_IMPORTED_MODULE_0___default().createElement("h3", { className: "jp-jobs-Heading" }, props.children);
        default:
            return react__WEBPACK_IMPORTED_MODULE_0___default().createElement("h1", { className: "jp-jobs-Heading" }, props.children);
    }
}


/***/ }),

/***/ "./lib/components/icon-buttons.js":
/*!****************************************!*\
  !*** ./lib/components/icon-buttons.js ***!
  \****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "AddButton": () => (/* binding */ AddButton),
/* harmony export */   "DeleteButton": () => (/* binding */ DeleteButton)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _mui_material__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @mui/material */ "webpack/sharing/consume/default/@mui/material/@mui/material");
/* harmony import */ var _mui_material__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_mui_material__WEBPACK_IMPORTED_MODULE_2__);



// Avoid extra vertical padding to force icon to be a square inside a circle
const zeroLineHeight = { lineHeight: 0 };
function DeleteButton(props) {
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_2__.IconButton, { "aria-label": "delete", onClick: props.onClick, title: props.title, sx: Object.assign(Object.assign({}, zeroLineHeight), props.addedStyle) },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.closeIcon.react, null)));
}
function AddButton(props) {
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_2__.IconButton, { onClick: props.onClick, title: props.title, sx: Object.assign(Object.assign({}, zeroLineHeight), props.addedStyle) },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.addIcon.react, null)));
}


/***/ }),

/***/ "./lib/components/icons.js":
/*!*********************************!*\
  !*** ./lib/components/icons.js ***!
  \*********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "calendarAddOnIcon": () => (/* binding */ calendarAddOnIcon),
/* harmony export */   "calendarMonthIcon": () => (/* binding */ calendarMonthIcon),
/* harmony export */   "eventNoteIcon": () => (/* binding */ eventNoteIcon),
/* harmony export */   "replayIcon": () => (/* binding */ replayIcon)
/* harmony export */ });
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _style_icons_calendar_add_on_svg__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../../style/icons/calendar-add-on.svg */ "./style/icons/calendar-add-on.svg");
/* harmony import */ var _style_icons_calendar_month_svg__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../../style/icons/calendar-month.svg */ "./style/icons/calendar-month.svg");
/* harmony import */ var _style_icons_event_note_svg__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../../style/icons/event-note.svg */ "./style/icons/event-note.svg");
/* harmony import */ var _style_icons_replay_svg__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ../../style/icons/replay.svg */ "./style/icons/replay.svg");
// This file is based on iconimports.ts in @jupyterlab/ui-components, but is manually generated.





const calendarAddOnIcon = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.LabIcon({
    name: 'jupyterlab-scheduler:calendar-add-on',
    svgstr: _style_icons_calendar_add_on_svg__WEBPACK_IMPORTED_MODULE_1__["default"]
});
const calendarMonthIcon = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.LabIcon({
    name: 'jupyterlab-scheduler:calendar-month',
    svgstr: _style_icons_calendar_month_svg__WEBPACK_IMPORTED_MODULE_2__["default"]
});
const eventNoteIcon = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.LabIcon({
    name: 'jupyterlab-scheduler:event-note',
    svgstr: _style_icons_event_note_svg__WEBPACK_IMPORTED_MODULE_3__["default"]
});
const replayIcon = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_0__.LabIcon({
    name: 'jupyterlab-scheduler:replay',
    svgstr: _style_icons_replay_svg__WEBPACK_IMPORTED_MODULE_4__["default"]
});


/***/ }),

/***/ "./lib/components/job-row.js":
/*!***********************************!*\
  !*** ./lib/components/job-row.js ***!
  \***********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "buildTableRow": () => (/* binding */ buildTableRow)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _mui_material_Stack__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @mui/material/Stack */ "./node_modules/@mui/material/esm/Stack/Stack.js");
/* harmony import */ var _mui_material_TableRow__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! @mui/material/TableRow */ "./node_modules/@mui/material/esm/TableRow/TableRow.js");
/* harmony import */ var _mui_material_TableCell__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! @mui/material/TableCell */ "./node_modules/@mui/material/esm/TableCell/TableCell.js");
/* harmony import */ var _hooks__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ../hooks */ "./lib/hooks.js");
/* harmony import */ var ___WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! .. */ "./lib/index.js");
/* harmony import */ var _icons__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./icons */ "./lib/components/icons.js");
/* harmony import */ var _output_format_picker__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./output-format-picker */ "./lib/components/output-format-picker.js");











function get_file_from_path(path) {
    return _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_2__.PathExt.basename(path);
}
function StopButton(props) {
    const trans = (0,_hooks__WEBPACK_IMPORTED_MODULE_4__.useTranslator)('jupyterlab');
    const buttonTitle = props.job.name
        ? trans.__('Stop "%1"', props.job.name)
        : trans.__('Stop job');
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { style: props.job.status !== 'IN_PROGRESS' ? { visibility: 'hidden' } : {} },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ToolbarButtonComponent, { onClick: props.clickHandler, tooltip: buttonTitle, icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__.stopIcon })));
}
function DeleteButton(props) {
    const trans = (0,_hooks__WEBPACK_IMPORTED_MODULE_4__.useTranslator)('jupyterlab');
    const buttonTitle = props.job.name
        ? trans.__('Delete "%1"', props.job.name)
        : trans.__('Delete job');
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ToolbarButtonComponent, { onClick: props.clickHandler, tooltip: buttonTitle, icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__.closeIcon }));
}
function RefillButton(props) {
    const trans = (0,_hooks__WEBPACK_IMPORTED_MODULE_4__.useTranslator)('jupyterlab');
    const buttonTitle = props.job.name
        ? trans.__('Rerun "%1" …', props.job.name)
        : trans.__('Rerun job …');
    // Retrieve the key from the parameters list or return a parameter with a null value
    function getParam(key) {
        var _a;
        return {
            name: key,
            value: (_a = props.job.parameters) === null || _a === void 0 ? void 0 : _a[key]
        };
    }
    // Convert the hash of parameters to an array.
    const jobParameters = props.job.parameters !== undefined
        ? Object.keys(props.job.parameters).map(key => getParam(key))
        : undefined;
    const clickHandler = () => {
        var _a;
        const newModel = {
            inputFile: props.job.input_uri,
            jobName: (_a = props.job.name) !== null && _a !== void 0 ? _a : '',
            outputPath: props.job.output_prefix,
            environment: props.job.runtime_environment_name,
            parameters: jobParameters
        };
        // Convert the list of output formats, if any, into a list for the initial state
        const jobOutputFormats = props.job.output_formats;
        const outputFormats = (0,_output_format_picker__WEBPACK_IMPORTED_MODULE_5__.outputFormatsForEnvironment)(props.environmentList, props.job.runtime_environment_name);
        if (jobOutputFormats && outputFormats) {
            newModel.outputFormats = outputFormats.filter(of => jobOutputFormats.some(jof => of.name === jof));
        }
        // Switch the view to the form.
        props.showCreateJob(newModel);
    };
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ToolbarButtonComponent, { onClick: clickHandler, tooltip: buttonTitle, icon: _icons__WEBPACK_IMPORTED_MODULE_6__.replayIcon }));
}
function Timestamp(props) {
    const create_date = props.job.create_time
        ? new Date(props.job.create_time)
        : null;
    const create_display_date = create_date
        ? create_date.toLocaleString()
        : null;
    return react__WEBPACK_IMPORTED_MODULE_0___default().createElement((react__WEBPACK_IMPORTED_MODULE_0___default().Fragment), null, create_display_date);
}
function OutputFiles(props) {
    if (props.job.status !== 'COMPLETED') {
        return null;
    }
    const trans = (0,_hooks__WEBPACK_IMPORTED_MODULE_4__.useTranslator)('jupyterlab');
    // Get all output files.
    const outputTypes = props.job.output_formats || ['ipynb'];
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement((react__WEBPACK_IMPORTED_MODULE_0___default().Fragment), null, outputTypes.map(outputType => {
        // Compose a specific link.
        const outputName = props.job.output_uri.replace(/ipynb$/, outputType);
        return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("a", { key: outputType, href: `/lab/tree/${outputName}`, title: trans.__('Open "%1"', outputName), onClick: e => props.openOnClick(e, outputName), style: { paddingRight: '1em' } }, outputType));
    })));
}
function buildTableRow(job, environmentList, app, showCreateJob, deleteRow, translateStatus, showDetailView) {
    const cellContents = [
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("a", { onClick: () => showDetailView(job.job_id) }, job.name),
        get_file_from_path(job.input_uri),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(OutputFiles, { job: job, openOnClick: (e, output_uri) => {
                e.preventDefault();
                app.commands.execute('docmanager:open', { path: output_uri });
            } }),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(Timestamp, { job: job }),
        translateStatus(job.status),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material_Stack__WEBPACK_IMPORTED_MODULE_7__["default"], { spacing: 1, direction: "row" },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(StopButton, { job: job, clickHandler: () => app.commands.execute(___WEBPACK_IMPORTED_MODULE_8__.CommandIDs.stopJob, {
                    id: job.job_id
                }) }),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(DeleteButton, { job: job, clickHandler: () => {
                    // optimistic delete for now, no verification on whether the delete
                    // succeeded
                    app.commands.execute(___WEBPACK_IMPORTED_MODULE_8__.CommandIDs.deleteJob, {
                        id: job.job_id
                    });
                    deleteRow(job.job_id);
                } }),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(RefillButton, { job: job, environmentList: environmentList, showCreateJob: showCreateJob }))
    ];
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material_TableRow__WEBPACK_IMPORTED_MODULE_9__["default"], null, cellContents.map((cellContent, idx) => (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material_TableCell__WEBPACK_IMPORTED_MODULE_10__["default"], { key: idx }, cellContent)))));
}


/***/ }),

/***/ "./lib/components/output-format-picker.js":
/*!************************************************!*\
  !*** ./lib/components/output-format-picker.js ***!
  \************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "OutputFormatPicker": () => (/* binding */ OutputFormatPicker),
/* harmony export */   "outputFormatsForEnvironment": () => (/* binding */ outputFormatsForEnvironment)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _mui_material__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @mui/material */ "webpack/sharing/consume/default/@mui/material/@mui/material");
/* harmony import */ var _mui_material__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_mui_material__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _stack__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./stack */ "./lib/components/stack.js");
/* harmony import */ var _cluster__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./cluster */ "./lib/components/cluster.js");




function outputFormatsForEnvironment(environmentList, environment) {
    const environmentObj = environmentList.find(env => env.name === environment);
    if (!environmentObj || !environmentObj['output_formats']) {
        return null;
    }
    return environmentObj['output_formats'];
}
function OutputFormatPicker(props) {
    const outputFormats = outputFormatsForEnvironment(props.environmentList, props.environment);
    if (outputFormats === null) {
        return null;
    }
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_stack__WEBPACK_IMPORTED_MODULE_2__.Stack, { size: 2 },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_1__.InputLabel, null, props.label),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_cluster__WEBPACK_IMPORTED_MODULE_3__.Cluster, { gap: 3, justifyContent: "flex-start" }, outputFormats.map((of, idx) => (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_1__.FormControlLabel, { key: idx, control: react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_1__.Checkbox, { defaultChecked: props.value.some(sof => of.name === sof.name), id: `${props.id}-${of.name}`, value: of.name, onChange: props.onChange }), label: of.label }))))));
}


/***/ }),

/***/ "./lib/components/parameters-picker.js":
/*!*********************************************!*\
  !*** ./lib/components/parameters-picker.js ***!
  \*********************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "ParametersPicker": () => (/* binding */ ParametersPicker)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _mui_material__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @mui/material */ "webpack/sharing/consume/default/@mui/material/@mui/material");
/* harmony import */ var _mui_material__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_mui_material__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _mui_system_Stack__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @mui/system/Stack */ "./node_modules/@mui/system/esm/Stack/Stack.js");
/* harmony import */ var _components_cluster__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ../components/cluster */ "./lib/components/cluster.js");
/* harmony import */ var _hooks__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../hooks */ "./lib/hooks.js");
/* harmony import */ var _icon_buttons__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./icon-buttons */ "./lib/components/icon-buttons.js");






function ParametersPicker(props) {
    const trans = (0,_hooks__WEBPACK_IMPORTED_MODULE_2__.useTranslator)('jupyterlab');
    const checkParameter = (e) => {
        const paramInputName = e.name;
        const paramMatch = paramInputName.match(/^parameter-(\d+)/);
        if (!paramMatch || paramMatch.length < 2) {
            return; // Invalid parameter name; should not happen
        }
        const paramIdx = parseInt(paramMatch[1]);
        const param = props.value[paramIdx];
        const invalid = param.name === '' && param.value !== '';
        props.handleErrorsChange(Object.assign(Object.assign({}, props.errors), { [`parameter-${paramIdx}-name`]: invalid
                ? trans.__('No name specified for this parameter.')
                : '' }));
    };
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_system_Stack__WEBPACK_IMPORTED_MODULE_3__["default"], { spacing: 2 },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_1__.InputLabel, null, props.label),
        props.value.map((param, paramIdx) => {
            var _a;
            const nameHasError = !!props.errors[`parameter-${paramIdx}-name`];
            return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_components_cluster__WEBPACK_IMPORTED_MODULE_4__.Cluster, { key: paramIdx, justifyContent: "flex-start", alignItems: "start" },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_1__.TextField, { name: `parameter-${paramIdx}-name`, value: param.name, type: "text", placeholder: trans.__('Name'), onBlur: e => checkParameter(e.target), error: nameHasError, helperText: (_a = props.errors[`parameter-${paramIdx}-name`]) !== null && _a !== void 0 ? _a : '', onChange: props.onChange }),
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_1__.TextField, { name: `parameter-${paramIdx}-value`, value: param.value, type: "text", placeholder: trans.__('Value'), onBlur: e => checkParameter(e.target), onChange: props.onChange }),
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_icon_buttons__WEBPACK_IMPORTED_MODULE_5__.DeleteButton, { onClick: () => props.removeParameter(paramIdx), title: trans.__('Delete this parameter'), addedStyle: { marginTop: '14px' } })));
        }),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_components_cluster__WEBPACK_IMPORTED_MODULE_4__.Cluster, { justifyContent: "flex-start" },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_icon_buttons__WEBPACK_IMPORTED_MODULE_5__.AddButton, { onClick: (e) => {
                    props.addParameter();
                    return false;
                }, title: trans.__('Add new parameter') }))));
}


/***/ }),

/***/ "./lib/components/running-jobs-indicator.js":
/*!**************************************************!*\
  !*** ./lib/components/running-jobs-indicator.js ***!
  \**************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "RunningJobsIndicator": () => (/* binding */ RunningJobsIndicator),
/* harmony export */   "RunningJobsIndicatorComponent": () => (/* binding */ RunningJobsIndicatorComponent)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/statusbar */ "webpack/sharing/consume/default/@jupyterlab/statusbar");
/* harmony import */ var _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _icons__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./icons */ "./lib/components/icons.js");
/* harmony import */ var _hooks__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ../hooks */ "./lib/hooks.js");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__);






function RunningJobsIndicatorComponent(props) {
    const runningJobs = props.runningJobs;
    // Don't display a status bar indicator if there are no running jobs (0 or undefined).
    if (!runningJobs) {
        return null;
    }
    const trans = (0,_hooks__WEBPACK_IMPORTED_MODULE_4__.useTranslator)('jupyterlab');
    const itemTitle = runningJobs > 1
        ? trans.__('%1 jobs running', runningJobs)
        : trans.__('%1 job running', runningJobs);
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_2__.interactiveItem, style: { paddingLeft: '4px', paddingRight: '4px' } },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_2__.GroupItem, { spacing: 4, title: itemTitle, onClick: props.handleClick },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_2__.TextItem, { source: `${runningJobs}` }),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_3__.LabIcon.resolveReact, { icon: _icons__WEBPACK_IMPORTED_MODULE_5__.calendarMonthIcon, tag: "span" }))));
}
function RunningJobsIndicator(props) {
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.UseSignal, { signal: props.model.inProgressJobCountChanged }, (_, newCount) => (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(RunningJobsIndicatorComponent, { handleClick: props.onClick, runningJobs: newCount }))));
}


/***/ }),

/***/ "./lib/components/stack.js":
/*!*********************************!*\
  !*** ./lib/components/stack.js ***!
  \*********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "Stack": () => (/* binding */ Stack)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);

function Stack(props) {
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { className: `jp-jobs-Stack size-${props.size || 1}` }, props.children));
}


/***/ }),

/***/ "./lib/context.js":
/*!************************!*\
  !*** ./lib/context.js ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_1__);


// Context to be overridden with JupyterLab context
const TranslatorContext = react__WEBPACK_IMPORTED_MODULE_1___default().createContext(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_0__.nullTranslator);
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (TranslatorContext);


/***/ }),

/***/ "./lib/handler.js":
/*!************************!*\
  !*** ./lib/handler.js ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "Scheduler": () => (/* binding */ Scheduler),
/* harmony export */   "SchedulerService": () => (/* binding */ SchedulerService)
/* harmony export */ });
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/services */ "webpack/sharing/consume/default/@jupyterlab/services");
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__);


const API_NAMESPACE = 'scheduler';
class SchedulerService {
    constructor(options) {
        this.serverSettings =
            options.serverSettings || _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.makeSettings();
    }
    async getJobDefinitions(definition_id) {
        let data;
        let query = '';
        if (definition_id) {
            query = `/${definition_id}`;
        }
        try {
            data = await requestAPI(this.serverSettings, `job_definitions${query}`, {
                method: 'GET'
            });
        }
        catch (e) {
            console.error(e);
        }
        return data;
    }
    async createJobDefinition(definition) {
        let data;
        try {
            data = await requestAPI(this.serverSettings, 'job_definitions', {
                method: 'POST',
                body: JSON.stringify(definition)
            });
        }
        catch (e) {
            console.error(e);
        }
        return data;
    }
    async getJob(job_id) {
        let data;
        let query = '';
        query = `/${job_id}`;
        try {
            data = await requestAPI(this.serverSettings, `jobs${query}`, {
                method: 'GET'
            });
        }
        catch (e) {
            console.error(e);
        }
        return data;
    }
    async getJobs(jobQuery, job_id) {
        let data;
        let query = '';
        if (job_id) {
            query = `/${job_id}`;
        }
        else if (jobQuery) {
            query =
                '?' +
                    Object.keys(jobQuery)
                        .map(prop => {
                        if (prop === 'sort_by') {
                            const sortList = jobQuery.sort_by;
                            if (sortList === undefined) {
                                return null;
                            }
                            // Serialize sort_by as a series of parameters in the firm dir(name)
                            // where 'dir' is the direction and 'name' the sort field
                            return sortList
                                .map(sort => `sort_by=${encodeURIComponent(sort.direction)}(${encodeURIComponent(sort.name)})`)
                                .join('&');
                        }
                        // eslint-disable-next-line @typescript-eslint/ban-ts-comment
                        // @ts-ignore
                        const value = jobQuery[prop];
                        return `${encodeURIComponent(prop)}=${encodeURIComponent(value)}`;
                    })
                        .join('&');
        }
        try {
            data = await requestAPI(this.serverSettings, `jobs${query}`, {
                method: 'GET'
            });
        }
        catch (e) {
            console.error(e);
        }
        return data;
    }
    async getjobCount(status) {
        let data = { count: 0 }; // Fail safe
        let query = '';
        if (status) {
            query = `?status=${encodeURIComponent(status)}`;
        }
        try {
            data = await requestAPI(this.serverSettings, `jobs/count${query}`, {
                method: 'GET'
            });
        }
        catch (e) {
            console.error(e);
        }
        return data.count;
    }
    async createJob(model) {
        let data;
        try {
            data = await requestAPI(this.serverSettings, 'jobs', {
                method: 'POST',
                body: JSON.stringify(model)
            });
        }
        catch (e) {
            console.error(e);
        }
        return data;
    }
    async setJobStatus(job_id, status) {
        let data;
        try {
            data = await requestAPI(this.serverSettings, `jobs/${job_id}`, {
                method: 'PATCH',
                body: JSON.stringify({ status })
            });
        }
        catch (e) {
            console.error(e);
        }
        return data;
    }
    async getRuntimeEnvironments() {
        let data;
        try {
            data = await requestAPI(this.serverSettings, 'runtime_environments', {
                method: 'GET'
            });
        }
        catch (e) {
            console.error(e);
        }
        return data;
    }
    async deleteJob(job_id) {
        try {
            await requestAPI(this.serverSettings, `jobs/${job_id}`, {
                method: 'DELETE'
            });
        }
        catch (e) {
            console.error(e);
        }
    }
}
/**
 * Call the API extension
 *
 * @param endPoint API REST end point for the extension
 * @param init Initial values for the request
 * @param expectData Is response data expected
 * @returns The response body interpreted as JSON
 */
async function requestAPI(settings, endPoint = '', init = {}, expectData = true) {
    // Make request to Jupyter API
    const requestUrl = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__.URLExt.join(settings.baseUrl, API_NAMESPACE, endPoint);
    let response;
    try {
        response = await _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.makeRequest(requestUrl, init, settings);
    }
    catch (error) {
        throw new _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.NetworkError(error);
    }
    let data = await response.text();
    if (expectData && data.length > 0) {
        try {
            data = JSON.parse(data);
        }
        catch (error) {
            console.error('Not a JSON response body.', response);
        }
    }
    if (!response.ok) {
        throw new _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.ResponseError(response, data.message || data);
    }
    return data;
}
var Scheduler;
(function (Scheduler) {
    let SortDirection;
    (function (SortDirection) {
        SortDirection["ASC"] = "asc";
        SortDirection["DESC"] = "desc";
    })(SortDirection = Scheduler.SortDirection || (Scheduler.SortDirection = {}));
})(Scheduler || (Scheduler = {}));


/***/ }),

/***/ "./lib/hooks.js":
/*!**********************!*\
  !*** ./lib/hooks.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "useTranslator": () => (/* binding */ useTranslator)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _context__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./context */ "./lib/context.js");


function useTranslator(bundleId) {
    const translator = (0,react__WEBPACK_IMPORTED_MODULE_0__.useContext)(_context__WEBPACK_IMPORTED_MODULE_1__["default"]);
    return translator.load(bundleId);
}


/***/ }),

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "CommandIDs": () => (/* binding */ CommandIDs),
/* harmony export */   "NotebookJobsPanelId": () => (/* binding */ NotebookJobsPanelId),
/* harmony export */   "Scheduler": () => (/* reexport safe */ _tokens__WEBPACK_IMPORTED_MODULE_8__.Scheduler),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/application */ "webpack/sharing/consume/default/@jupyterlab/application");
/* harmony import */ var _jupyterlab_application__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_application__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/filebrowser */ "webpack/sharing/consume/default/@jupyterlab/filebrowser");
/* harmony import */ var _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_3__);
/* harmony import */ var _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @jupyterlab/launcher */ "webpack/sharing/consume/default/@jupyterlab/launcher");
/* harmony import */ var _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @jupyterlab/statusbar */ "webpack/sharing/consume/default/@jupyterlab/statusbar");
/* harmony import */ var _jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_5___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_5__);
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @jupyterlab/translation */ "webpack/sharing/consume/default/@jupyterlab/translation");
/* harmony import */ var _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_6___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_translation__WEBPACK_IMPORTED_MODULE_6__);
/* harmony import */ var _lumino_polling__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @lumino/polling */ "webpack/sharing/consume/default/@lumino/polling/@lumino/polling");
/* harmony import */ var _lumino_polling__WEBPACK_IMPORTED_MODULE_7___default = /*#__PURE__*/__webpack_require__.n(_lumino_polling__WEBPACK_IMPORTED_MODULE_7__);
/* harmony import */ var _components_running_jobs_indicator__WEBPACK_IMPORTED_MODULE_14__ = __webpack_require__(/*! ./components/running-jobs-indicator */ "./lib/components/running-jobs-indicator.js");
/* harmony import */ var _handler__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! ./handler */ "./lib/handler.js");
/* harmony import */ var _model__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! ./model */ "./lib/model.js");
/* harmony import */ var _notebook_jobs_panel__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(/*! ./notebook-jobs-panel */ "./lib/notebook-jobs-panel.js");
/* harmony import */ var _components_icons__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__(/*! ./components/icons */ "./lib/components/icons.js");
/* harmony import */ var _tokens__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ./tokens */ "./lib/tokens.js");
/* harmony import */ var _advanced_options__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! ./advanced-options */ "./lib/advanced-options.js");















var CommandIDs;
(function (CommandIDs) {
    CommandIDs.deleteJob = 'scheduling:delete-job';
    CommandIDs.runNotebook = 'scheduling:run-notebook';
    CommandIDs.showNotebookJobs = 'scheduling:show-notebook-jobs';
    CommandIDs.stopJob = 'scheduling:stop-job';
})(CommandIDs || (CommandIDs = {}));
const NotebookJobsPanelId = 'notebook-jobs-panel';

/**
 * Initialization data for the jupyterlab-scheduler extension.
 */
const schedulerPlugin = {
    id: '@jupyterlab/scheduler:plugin',
    requires: [
        _jupyterlab_filebrowser__WEBPACK_IMPORTED_MODULE_3__.IFileBrowserFactory,
        _jupyterlab_translation__WEBPACK_IMPORTED_MODULE_6__.ITranslator,
        _jupyterlab_application__WEBPACK_IMPORTED_MODULE_1__.ILayoutRestorer,
        _tokens__WEBPACK_IMPORTED_MODULE_8__.Scheduler.IAdvancedOptions
    ],
    optional: [_jupyterlab_statusbar__WEBPACK_IMPORTED_MODULE_5__.IStatusBar, _jupyterlab_launcher__WEBPACK_IMPORTED_MODULE_4__.ILauncher],
    autoStart: true,
    activate: activatePlugin
};
// Disable this plugin and replace with custom plugin to change the advanced options UI
const advancedOptions = {
    id: '@jupyterlab/scheduler:IAdvancedOptions',
    autoStart: true,
    provides: _tokens__WEBPACK_IMPORTED_MODULE_8__.Scheduler.IAdvancedOptions,
    activate: (app) => {
        return _advanced_options__WEBPACK_IMPORTED_MODULE_9__["default"];
    }
};
function getSelectedItem(widget) {
    if (widget === null) {
        return null;
    }
    // Get the first selected item.
    const firstItem = widget.selectedItems().next();
    if (firstItem === null || firstItem === undefined) {
        return null;
    }
    return firstItem;
}
function getSelectedFilePath(widget) {
    const selectedItem = getSelectedItem(widget);
    if (selectedItem === null) {
        return null;
    }
    return selectedItem.path;
}
function getSelectedFileName(widget) {
    const selectedItem = getSelectedItem(widget);
    if (selectedItem === null) {
        return null;
    }
    return selectedItem.name;
}
let scheduledJobsListingModel = null;
async function getNotebookJobsListingModel() {
    if (scheduledJobsListingModel) {
        return scheduledJobsListingModel;
    }
    const api = new _handler__WEBPACK_IMPORTED_MODULE_10__.SchedulerService({});
    const jobsResponse = await api.getJobs({});
    scheduledJobsListingModel = new _model__WEBPACK_IMPORTED_MODULE_11__.NotebookJobsListingModel(jobsResponse.jobs);
    return scheduledJobsListingModel;
}
async function activatePlugin(app, browserFactory, translator, restorer, advancedOptions, statusBar, launcher) {
    // first, validate presence of dependencies
    if (!statusBar) {
        return;
    }
    const { commands } = app;
    const trans = translator.load('jupyterlab');
    const { tracker } = browserFactory;
    const api = new _handler__WEBPACK_IMPORTED_MODULE_10__.SchedulerService({});
    const widgetTracker = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__.WidgetTracker({
        namespace: 'jupyterlab-scheduler'
    });
    restorer.restore(widgetTracker, {
        command: CommandIDs.showNotebookJobs,
        name: () => 'jupyterlab-scheduler'
    });
    commands.addCommand(CommandIDs.deleteJob, {
        execute: async (args) => {
            const id = args['id'];
            await api.deleteJob(id);
        },
        // TODO: Use args to name command dynamically
        label: trans.__('Delete Job')
    });
    let mainAreaWidget;
    let jobsPanel;
    const showJobsPane = async (view) => {
        if (!mainAreaWidget || mainAreaWidget.isDisposed) {
            // Create new jobs panel widget
            jobsPanel = new _notebook_jobs_panel__WEBPACK_IMPORTED_MODULE_12__.NotebookJobsPanel({
                app,
                translator,
                advancedOptions: advancedOptions
            });
            // Create new main area widget
            mainAreaWidget = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__.MainAreaWidget({
                content: jobsPanel
            });
            mainAreaWidget.content.model.jobsView = view;
            mainAreaWidget.id = NotebookJobsPanelId;
            mainAreaWidget.title.icon = _components_icons__WEBPACK_IMPORTED_MODULE_13__.calendarMonthIcon;
            mainAreaWidget.title.label = trans.__('Notebook Jobs');
            mainAreaWidget.title.closable = true;
        }
        if (!widgetTracker.has(mainAreaWidget)) {
            // Track the state of the widget for later restoration
            widgetTracker.add(mainAreaWidget);
        }
        if (!mainAreaWidget.isAttached) {
            app.shell.add(mainAreaWidget, 'main');
        }
        mainAreaWidget.content.model.jobsView = view;
        mainAreaWidget.content.update();
        app.shell.activateById(mainAreaWidget.id);
    };
    commands.addCommand(CommandIDs.showNotebookJobs, {
        execute: async () => showJobsPane('ListJobs'),
        label: trans.__('Notebook Jobs'),
        icon: _components_icons__WEBPACK_IMPORTED_MODULE_13__.eventNoteIcon
    });
    commands.addCommand(CommandIDs.runNotebook, {
        execute: async () => {
            var _a, _b;
            await showJobsPane('CreateJob');
            const model = jobsPanel === null || jobsPanel === void 0 ? void 0 : jobsPanel.model;
            if (!model) {
                return;
            }
            const widget = tracker.currentWidget;
            const filePath = (_a = getSelectedFilePath(widget)) !== null && _a !== void 0 ? _a : '';
            const fileName = (_b = getSelectedFileName(widget)) !== null && _b !== void 0 ? _b : '';
            // Update the job form inside the notebook jobs widget
            const newModel = {
                inputFile: filePath,
                jobName: fileName,
                outputPath: '',
                environment: ''
            };
            model.createJobModel = newModel;
        },
        label: trans.__('Create Notebook Job'),
        icon: _components_icons__WEBPACK_IMPORTED_MODULE_13__.calendarAddOnIcon
    });
    commands.addCommand(CommandIDs.stopJob, {
        execute: async (args) => {
            const id = args['id'];
            await api.setJobStatus(id, 'STOPPED');
        },
        // TODO: Use args to name command dynamically
        label: trans.__('Stop Job')
    });
    // validate presence of status bar
    if (!statusBar) {
        return;
    }
    const scheduledJobsListingModel = await getNotebookJobsListingModel();
    statusBar.registerStatusItem('jupyterlab-scheduler:status', {
        align: 'middle',
        item: _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_2__.ReactWidget.create(react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_components_running_jobs_indicator__WEBPACK_IMPORTED_MODULE_14__.RunningJobsIndicator, { onClick: async () => showJobsPane('ListJobs'), model: scheduledJobsListingModel }))
    });
    const statusPoll = new _lumino_polling__WEBPACK_IMPORTED_MODULE_7__.Poll({
        factory: async () => {
            const model = jobsPanel === null || jobsPanel === void 0 ? void 0 : jobsPanel.model;
            if (!model) {
                return;
            }
            const jobCount = await api.getjobCount('IN_PROGRESS');
            model.jobCount = jobCount;
        },
        frequency: { interval: 1000, backoff: false }
    });
    statusPoll.start();
    // Add to launcher
    if (launcher) {
        launcher.add({
            command: CommandIDs.showNotebookJobs
        });
    }
}
const plugins = [
    schedulerPlugin,
    advancedOptions
];
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugins);


/***/ }),

/***/ "./lib/mainviews/create-job.js":
/*!*************************************!*\
  !*** ./lib/mainviews/create-job.js ***!
  \*************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "CreateJob": () => (/* binding */ CreateJob)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _components_heading__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ../components/heading */ "./lib/components/heading.js");
/* harmony import */ var _components_cluster__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__(/*! ../components/cluster */ "./lib/components/cluster.js");
/* harmony import */ var _components_compute_type_picker__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! ../components/compute-type-picker */ "./lib/components/compute-type-picker.js");
/* harmony import */ var _components_environment_picker__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! ../components/environment-picker */ "./lib/components/environment-picker.js");
/* harmony import */ var _components_output_format_picker__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ../components/output-format-picker */ "./lib/components/output-format-picker.js");
/* harmony import */ var _components_parameters_picker__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(/*! ../components/parameters-picker */ "./lib/components/parameters-picker.js");
/* harmony import */ var _handler__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ../handler */ "./lib/handler.js");
/* harmony import */ var _hooks__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../hooks */ "./lib/hooks.js");
/* harmony import */ var _mui_material_Button__WEBPACK_IMPORTED_MODULE_14__ = __webpack_require__(/*! @mui/material/Button */ "./node_modules/@mui/material/esm/Button/Button.js");
/* harmony import */ var _mui_system_Box__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @mui/system/Box */ "./node_modules/@mui/system/esm/Box/Box.js");
/* harmony import */ var _mui_system_Stack__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @mui/system/Stack */ "./node_modules/@mui/system/esm/Stack/Stack.js");
/* harmony import */ var _mui_material_TextField__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! @mui/material/TextField */ "./node_modules/@mui/material/esm/TextField/TextField.js");
/* harmony import */ var _mui_material__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @mui/material */ "webpack/sharing/consume/default/@mui/material/@mui/material");
/* harmony import */ var _mui_material__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_mui_material__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__);















function parameterNameMatch(elementName) {
    const parameterNameMatch = elementName.match(/^parameter-(\d+)-name$/);
    if (parameterNameMatch === null) {
        return null;
    }
    return parseInt(parameterNameMatch[1]);
}
function parameterValueMatch(elementName) {
    const parameterValueMatch = elementName.match(/^parameter-(\d+)-value$/);
    if (parameterValueMatch === null) {
        return null;
    }
    return parseInt(parameterValueMatch[1]);
}
function CreateJob(props) {
    var _a;
    const trans = (0,_hooks__WEBPACK_IMPORTED_MODULE_3__.useTranslator)('jupyterlab');
    // Cache environment list.
    const [environmentList, setEnvironmentList] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)([]);
    // A mapping from input names to error messages.
    // If an error message is "truthy" (i.e., not null or ''), we should display the
    // input in an error state and block form submission.
    const [errors, setErrors] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)({});
    const api = (0,react__WEBPACK_IMPORTED_MODULE_0__.useMemo)(() => new _handler__WEBPACK_IMPORTED_MODULE_4__.SchedulerService({}), []);
    // Retrieve the environment list once.
    (0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)(() => {
        const setList = async () => {
            setEnvironmentList(await api.getRuntimeEnvironments());
        };
        setList();
    }, []);
    // If any error message is "truthy" (not null or empty), the form should not be submitted.
    const anyErrors = Object.keys(errors).some(key => !!errors[key]);
    const handleInputChange = (event) => {
        const target = event.target;
        const parameterNameIdx = parameterNameMatch(target.name);
        const parameterValueIdx = parameterValueMatch(target.name);
        const newParams = props.model.parameters || [];
        if (parameterNameIdx !== null) {
            newParams[parameterNameIdx].name = target.value;
            props.handleModelChange(Object.assign(Object.assign({}, props.model), { parameters: newParams }));
        }
        else if (parameterValueIdx !== null) {
            newParams[parameterValueIdx].value = target.value;
            props.handleModelChange(Object.assign(Object.assign({}, props.model), { parameters: newParams }));
        }
        else {
            const value = target.type === 'checkbox' ? target.checked : target.value;
            const name = target.name;
            props.handleModelChange(Object.assign(Object.assign({}, props.model), { [name]: value }));
        }
    };
    const handleSelectChange = (event) => {
        var _a;
        const target = event.target;
        // if setting the environment, default the compute type to its first value (if any are presnt)
        if (target.name === 'environment') {
            const envObj = environmentList.find(env => env.name === target.value);
            props.handleModelChange(Object.assign(Object.assign({}, props.model), { environment: target.value, computeType: (_a = envObj === null || envObj === void 0 ? void 0 : envObj.compute_types) === null || _a === void 0 ? void 0 : _a[0] }));
        }
        else {
            // otherwise, just set the model
            props.handleModelChange(Object.assign(Object.assign({}, props.model), { [target.name]: target.value }));
        }
    };
    const handleOutputFormatsChange = (event) => {
        const outputFormatsList = (0,_components_output_format_picker__WEBPACK_IMPORTED_MODULE_5__.outputFormatsForEnvironment)(environmentList, props.model.environment);
        if (outputFormatsList === null) {
            return; // No data about output formats; give up
        }
        const formatName = event.target.value;
        const isChecked = event.target.checked;
        const wasChecked = props.model.outputFormats
            ? props.model.outputFormats.some(of => of.name === formatName)
            : false;
        const oldOutputFormats = props.model.outputFormats || [];
        // Go from unchecked to checked
        if (isChecked && !wasChecked) {
            // Get the output format matching the given name
            const newFormat = outputFormatsList.find(of => of.name === formatName);
            if (newFormat) {
                props.handleModelChange(Object.assign(Object.assign({}, props.model), { outputFormats: [...oldOutputFormats, newFormat] }));
            }
        }
        // Go from checked to unchecked
        else if (!isChecked && wasChecked) {
            props.handleModelChange(Object.assign(Object.assign({}, props.model), { outputFormats: oldOutputFormats.filter(of => of.name !== formatName) }));
        }
        // If no change in checkedness, don't do anything
    };
    const submitCreateJobRequest = async (event) => {
        if (anyErrors) {
            console.error('User attempted to submit a createJob request; button should have been disabled');
            return;
        }
        // Serialize parameters as an object.
        const jobOptions = {
            name: props.model.jobName,
            input_uri: props.model.inputFile,
            output_prefix: props.model.outputPath,
            runtime_environment_name: props.model.environment,
            compute_type: props.model.computeType,
            idempotency_token: props.model.idempotencyToken,
            tags: props.model.tags,
            runtime_environment_parameters: props.model.runtimeEnvironmentParameters
        };
        if (props.model.parameters !== undefined) {
            const jobParameters = {};
            props.model.parameters.forEach(param => {
                const { name, value } = param;
                if (jobParameters[name] !== undefined) {
                    console.error('Parameter ' +
                        name +
                        ' already set to ' +
                        jobParameters[name] +
                        ' and is about to be set again to ' +
                        value);
                }
                else {
                    jobParameters[name] = value;
                }
            });
            jobOptions.parameters = jobParameters;
        }
        if (props.model.outputFormats !== undefined) {
            jobOptions.output_formats = props.model.outputFormats.map(entry => entry.name);
        }
        api.createJob(jobOptions).then(response => {
            props.toggleView();
        });
    };
    const removeParameter = (idx) => {
        const newParams = props.model.parameters || [];
        newParams.splice(idx, 1);
        const newErrors = {};
        for (const formKey in errors) {
            const paramMatch = formKey.match(/^parameter-(\d+)/);
            const paramIdx = paramMatch && paramMatch.length >= 2 ? parseInt(paramMatch[1]) : -1;
            if (paramIdx === -1 || paramIdx < idx) {
                // restore errors associated with params before deleted param and all
                // other form fields
                newErrors[formKey] = errors[formKey];
                continue;
            }
            if (paramIdx === idx) {
                // ignore errors associated with deleted param
                continue;
            }
            // otherwise, restore errors with params after deleted param by offsetting
            // their index by -1
            newErrors[`parameter-${paramIdx - 1}-name`] =
                errors[`parameter-${paramIdx}-name`];
        }
        props.handleModelChange(Object.assign(Object.assign({}, props.model), { parameters: newParams }));
        setErrors(newErrors);
    };
    const addParameter = () => {
        const newParams = props.model.parameters || [];
        newParams.push({ name: '', value: '' });
        props.handleModelChange(Object.assign(Object.assign({}, props.model), { parameters: newParams }));
    };
    // If the text field is blank, record an error.
    const validateEmpty = (e) => {
        const inputName = e.name;
        const inputValue = e.value;
        if (inputValue === '') {
            // blank
            setErrors(Object.assign(Object.assign({}, errors), { [inputName]: trans.__('You must provide a value.') }));
        }
        else {
            setErrors(Object.assign(Object.assign({}, errors), { [inputName]: '' }));
        }
    };
    // Is there a truthy (non-empty) error for this field?
    const hasError = (inputName) => {
        return !!errors[inputName];
    };
    const formPrefix = 'jp-create-job-';
    const cantSubmit = trans.__('One or more of the fields has an error.');
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_system_Box__WEBPACK_IMPORTED_MODULE_6__["default"], { sx: { p: 4 } },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("form", { className: `${formPrefix}form`, onSubmit: e => e.preventDefault() },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_system_Stack__WEBPACK_IMPORTED_MODULE_7__["default"], { spacing: 4 },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_components_heading__WEBPACK_IMPORTED_MODULE_8__.Heading, { level: 1 }, "Create Job"),
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material_TextField__WEBPACK_IMPORTED_MODULE_9__["default"], { label: trans.__('Job name'), variant: "outlined", onChange: handleInputChange, value: props.model.jobName, id: `${formPrefix}jobName`, name: "jobName" }),
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material_TextField__WEBPACK_IMPORTED_MODULE_9__["default"], { label: trans.__('Input file'), variant: "outlined", onChange: handleInputChange, value: props.model.inputFile, id: `${formPrefix}inputFile`, onBlur: e => validateEmpty(e.target), error: hasError('inputFile'), helperText: (_a = errors['inputFile']) !== null && _a !== void 0 ? _a : '', name: "inputFile" }),
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material_TextField__WEBPACK_IMPORTED_MODULE_9__["default"], { label: trans.__('Output path'), variant: "outlined", onChange: handleInputChange, value: props.model.outputPath, id: `${formPrefix}outputPath`, name: "outputPath" }),
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_components_environment_picker__WEBPACK_IMPORTED_MODULE_10__.EnvironmentPicker, { label: trans.__('Environment'), name: 'environment', id: `${formPrefix}environment`, onChange: handleSelectChange, environmentList: environmentList, initialValue: props.model.environment }),
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_components_output_format_picker__WEBPACK_IMPORTED_MODULE_5__.OutputFormatPicker, { label: trans.__('Output formats'), name: "outputFormat", id: `${formPrefix}outputFormat`, onChange: handleOutputFormatsChange, environmentList: environmentList, environment: props.model.environment, value: props.model.outputFormats || [] }),
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_components_compute_type_picker__WEBPACK_IMPORTED_MODULE_11__.ComputeTypePicker, { label: trans.__('Compute type'), name: "computeType", id: `${formPrefix}computeType`, onChange: handleSelectChange, environmentList: environmentList, environment: props.model.environment, value: props.model.computeType }),
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_components_parameters_picker__WEBPACK_IMPORTED_MODULE_12__.ParametersPicker, { label: trans.__('Parameters'), name: 'parameters', id: `${formPrefix}parameters`, value: props.model.parameters || [], onChange: handleInputChange, addParameter: addParameter, removeParameter: removeParameter, formPrefix: formPrefix, errors: errors, handleErrorsChange: setErrors }),
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_1__.Accordion, { defaultExpanded: false },
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_1__.AccordionSummary, { expandIcon: react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__.caretDownIcon.react, null), "aria-controls": "panel-content", id: "panel-header" },
                        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_1__.FormLabel, { component: "legend" }, trans.__('Additional options'))),
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_1__.AccordionDetails, { id: `${formPrefix}create-panel-content` },
                        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(props.advancedOptions, { jobsView: 'CreateJob', model: props.model, handleModelChange: props.handleModelChange, errors: errors, handleErrorsChange: setErrors }))),
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_components_cluster__WEBPACK_IMPORTED_MODULE_13__.Cluster, { gap: 3, justifyContent: "flex-end" },
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material_Button__WEBPACK_IMPORTED_MODULE_14__["default"], { variant: "outlined", onClick: props.toggleView }, trans.__('Cancel')),
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material_Button__WEBPACK_IMPORTED_MODULE_14__["default"], { variant: "contained", onClick: (e) => {
                            submitCreateJobRequest(e);
                            return false;
                        }, disabled: anyErrors, title: anyErrors ? cantSubmit : '' }, trans.__('Create')))))));
}


/***/ }),

/***/ "./lib/mainviews/job-detail.js":
/*!*************************************!*\
  !*** ./lib/mainviews/job-detail.js ***!
  \*************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "JobDetail": () => (/* binding */ JobDetail)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _model__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ../model */ "./lib/model.js");
/* harmony import */ var _hooks__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../hooks */ "./lib/hooks.js");
/* harmony import */ var _components_heading__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! ../components/heading */ "./lib/components/heading.js");
/* harmony import */ var _handler__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../handler */ "./lib/handler.js");
/* harmony import */ var _mui_material_Box__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! @mui/material/Box */ "./node_modules/@mui/material/esm/Box/Box.js");
/* harmony import */ var _mui_material_Button__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @mui/material/Button */ "./node_modules/@mui/material/esm/Button/Button.js");
/* harmony import */ var _mui_material_Breadcrumbs__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @mui/material/Breadcrumbs */ "./node_modules/@mui/material/esm/Breadcrumbs/Breadcrumbs.js");
/* harmony import */ var _mui_material_Link__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! @mui/material/Link */ "./node_modules/@mui/material/esm/Link/Link.js");
/* harmony import */ var _mui_material_Stack__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! @mui/material/Stack */ "./node_modules/@mui/material/esm/Stack/Stack.js");
/* harmony import */ var _mui_material__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @mui/material */ "webpack/sharing/consume/default/@mui/material/@mui/material");
/* harmony import */ var _mui_material__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_mui_material__WEBPACK_IMPORTED_MODULE_1__);











const TextFieldStyled = (props) => (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_1__.TextField, Object.assign({}, props, { variant: "outlined", InputProps: { readOnly: true } })));
function JobDetail(props) {
    var _a, _b, _c, _d, _e;
    const [loading, setLoading] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)(true);
    const [outputFormatsStrings, setOutputFormatsStrings] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)([]);
    const trans = (0,_hooks__WEBPACK_IMPORTED_MODULE_2__.useTranslator)('jupyterlab');
    const ss = new _handler__WEBPACK_IMPORTED_MODULE_3__.SchedulerService({});
    const updateJob = async () => {
        var _a;
        const jobFromService = await ss.getJob(props.model.jobId);
        setOutputFormatsStrings((_a = jobFromService.output_formats) !== null && _a !== void 0 ? _a : []);
        const newModel = Object.assign(Object.assign({}, props.model), (0,_model__WEBPACK_IMPORTED_MODULE_4__.convertDescribeJobtoJobDetail)(jobFromService));
        props.handleModelChange(newModel);
        setLoading(false);
    };
    const handleRerunJob = () => {
        var _a;
        const initialState = {
            jobName: props.model.jobName,
            inputFile: props.model.inputFile,
            outputPath: (_a = props.model.outputPrefix) !== null && _a !== void 0 ? _a : '',
            environment: props.model.environment,
            parameters: props.model.parameters
        };
        props.setCreateJobModel(initialState);
        props.setView('CreateJob');
    };
    const handleDeleteJob = async () => {
        var _a;
        await ss.deleteJob((_a = props.model.jobId) !== null && _a !== void 0 ? _a : '');
        props.setView('ListJobs');
    };
    const handleStopJob = async () => {
        await props.app.commands.execute('scheduling:stop-job', {
            id: props.model.jobId
        });
        updateJob();
    };
    const timestampLocalize = (time) => {
        if (time === '') {
            return '';
        }
        else {
            const display_date = new Date(time);
            const local_display_date = display_date
                ? display_date.toLocaleString()
                : '';
            return local_display_date;
        }
    };
    const Loading = (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material_Stack__WEBPACK_IMPORTED_MODULE_5__["default"], { direction: "row", justifyContent: "center" },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_1__.CircularProgress, { title: trans.__('Loading') })));
    const BreadcrumbsStyled = () => (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { role: "presentation" },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material_Breadcrumbs__WEBPACK_IMPORTED_MODULE_6__["default"], { "aria-label": "breadcrumb" },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material_Link__WEBPACK_IMPORTED_MODULE_7__["default"], { underline: "hover", color: "inherit", onClick: (_) => props.setView('ListJobs') }, trans.__('Notebook Jobs')),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_1__.Typography, { color: "text.primary" }, props.model.jobName))));
    const ButtonBar = (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material_Stack__WEBPACK_IMPORTED_MODULE_5__["default"], { direction: "row", gap: 2, justifyContent: "flex-end", flexWrap: 'wrap' },
        props.model.status === 'IN_PROGRESS' && (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material_Button__WEBPACK_IMPORTED_MODULE_8__["default"], { variant: "outlined", onClick: handleStopJob }, trans.__('Stop Job'))),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material_Button__WEBPACK_IMPORTED_MODULE_8__["default"], { variant: "outlined", onClick: handleRerunJob }, trans.__('Rerun Job')),
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material_Button__WEBPACK_IMPORTED_MODULE_8__["default"], { variant: "contained", color: "error", onClick: handleDeleteJob }, trans.__('Delete Job'))));
    const coreOptionsFields = [
        [
            { defaultValue: props.model.jobName, label: trans.__('Job name') },
            { defaultValue: props.model.jobId, label: trans.__('Job ID') }
        ],
        [
            {
                defaultValue: props.model.inputFile,
                label: trans.__('Input file')
            },
            {
                defaultValue: props.model.outputPath,
                label: trans.__('Output path')
            }
        ],
        [
            {
                defaultValue: props.model.environment,
                label: trans.__('Environment')
            },
            { defaultValue: (_a = props.model.status) !== null && _a !== void 0 ? _a : '', label: trans.__('Status') }
        ],
        [
            {
                defaultValue: timestampLocalize((_b = props.model.createTime) !== null && _b !== void 0 ? _b : ''),
                label: trans.__('Created at')
            },
            {
                defaultValue: timestampLocalize((_c = props.model.updateTime) !== null && _c !== void 0 ? _c : ''),
                label: trans.__('Updated at')
            }
        ],
        [
            {
                defaultValue: timestampLocalize((_d = props.model.startTime) !== null && _d !== void 0 ? _d : ''),
                label: trans.__('Start time')
            },
            {
                defaultValue: timestampLocalize((_e = props.model.endTime) !== null && _e !== void 0 ? _e : ''),
                label: trans.__('End time')
            }
        ]
    ];
    function OutputFile(props) {
        const outputName = props.outputPath.replace(/ipynb$/, props.outputType);
        return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material_Link__WEBPACK_IMPORTED_MODULE_7__["default"], { key: props.outputType, href: `/lab/tree/${outputName}`, title: trans.__('Open "%1"', outputName), onClick: (e) => {
                e.preventDefault();
                props.app.commands.execute('docmanager:open', {
                    path: outputName
                });
            }, style: { paddingRight: '1em' } }, outputName));
    }
    const CoreOptions = (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_1__.Card, null,
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_1__.CardContent, null,
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material_Stack__WEBPACK_IMPORTED_MODULE_5__["default"], { spacing: 4 },
                coreOptionsFields.map(propsRow => (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material_Stack__WEBPACK_IMPORTED_MODULE_5__["default"], { direction: 'row', gap: 2, flexWrap: 'wrap' }, propsRow.map(textProp => (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(TextFieldStyled, Object.assign({}, textProp, { style: {
                        flexGrow: 1
                    } }))))))),
                props.model.status === 'COMPLETED' && (react__WEBPACK_IMPORTED_MODULE_0___default().createElement((react__WEBPACK_IMPORTED_MODULE_0___default().Fragment), null,
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_1__.FormLabel, { component: "legend" }, trans.__('Output files')),
                    outputFormatsStrings.map(outputFormatString => (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(OutputFile, { outputType: outputFormatString, app: props.app, outputPath: props.model.outputPath })))))))));
    const Parameters = (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_1__.Card, null,
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_1__.CardContent, null,
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_1__.FormLabel, { sx: { mb: 4 }, component: "legend" }, trans.__('Parameters')),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material_Stack__WEBPACK_IMPORTED_MODULE_5__["default"], { spacing: 4 }, props.model.parameters &&
                props.model.parameters.map((parameter, idx) => (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material_Stack__WEBPACK_IMPORTED_MODULE_5__["default"], { key: idx, direction: 'row', gap: 2, flexWrap: 'wrap' },
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement(TextFieldStyled, { label: trans.__('Parameter name'), defaultValue: parameter.name, style: {
                            flexGrow: 1
                        } }),
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement(TextFieldStyled, { label: trans.__('Parameter value'), defaultValue: parameter.value, style: {
                            flexGrow: 1
                        } }))))))));
    const AdvancedOptions = (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_1__.Card, null,
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_1__.CardContent, null,
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material_Stack__WEBPACK_IMPORTED_MODULE_5__["default"], { component: "form", spacing: 4 },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material__WEBPACK_IMPORTED_MODULE_1__.FormLabel, { component: "legend" }, trans.__('Advanced Options')),
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(props.advancedOptions, { jobsView: 'JobDetail', model: props.model, handleModelChange: model => {
                        return;
                    }, errors: {}, handleErrorsChange: errors => {
                        return;
                    } })))));
    (0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)(() => {
        updateJob();
    }, []);
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material_Box__WEBPACK_IMPORTED_MODULE_9__["default"], { sx: { p: 4 } },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material_Stack__WEBPACK_IMPORTED_MODULE_5__["default"], { spacing: 4 },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(BreadcrumbsStyled, null),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_components_heading__WEBPACK_IMPORTED_MODULE_10__.Heading, { level: 1 }, trans.__('Job Detail')),
            loading ? (Loading) : (react__WEBPACK_IMPORTED_MODULE_0___default().createElement((react__WEBPACK_IMPORTED_MODULE_0___default().Fragment), null,
                ButtonBar,
                CoreOptions,
                Parameters,
                AdvancedOptions)))));
}


/***/ }),

/***/ "./lib/mainviews/list-jobs.js":
/*!************************************!*\
  !*** ./lib/mainviews/list-jobs.js ***!
  \************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "NotebookJobsList": () => (/* binding */ NotebookJobsList),
/* harmony export */   "NotebookJobsListBody": () => (/* binding */ NotebookJobsListBody),
/* harmony export */   "PAGE_SIZE": () => (/* binding */ PAGE_SIZE)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _hooks__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ../hooks */ "./lib/hooks.js");
/* harmony import */ var _components_job_row__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ../components/job-row */ "./lib/components/job-row.js");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _handler__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../handler */ "./lib/handler.js");
/* harmony import */ var _components_heading__WEBPACK_IMPORTED_MODULE_17__ = __webpack_require__(/*! ../components/heading */ "./lib/components/heading.js");
/* harmony import */ var _components_cluster__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ../components/cluster */ "./lib/components/cluster.js");
/* harmony import */ var _mui_material_styles__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @mui/material/styles */ "./node_modules/@mui/material/esm/styles/useTheme.js");
/* harmony import */ var _mui_material_Button__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! @mui/material/Button */ "./node_modules/@mui/material/esm/Button/Button.js");
/* harmony import */ var _mui_system_Box__WEBPACK_IMPORTED_MODULE_15__ = __webpack_require__(/*! @mui/system/Box */ "./node_modules/@mui/system/esm/Box/Box.js");
/* harmony import */ var _mui_system_Stack__WEBPACK_IMPORTED_MODULE_16__ = __webpack_require__(/*! @mui/system/Stack */ "./node_modules/@mui/system/esm/Stack/Stack.js");
/* harmony import */ var _mui_material_Table__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! @mui/material/Table */ "./node_modules/@mui/material/esm/Table/Table.js");
/* harmony import */ var _mui_material_TableContainer__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! @mui/material/TableContainer */ "./node_modules/@mui/material/esm/TableContainer/TableContainer.js");
/* harmony import */ var _mui_material_TableHead__WEBPACK_IMPORTED_MODULE_11__ = __webpack_require__(/*! @mui/material/TableHead */ "./node_modules/@mui/material/esm/TableHead/TableHead.js");
/* harmony import */ var _mui_material_TableBody__WEBPACK_IMPORTED_MODULE_12__ = __webpack_require__(/*! @mui/material/TableBody */ "./node_modules/@mui/material/esm/TableBody/TableBody.js");
/* harmony import */ var _mui_material_TableCell__WEBPACK_IMPORTED_MODULE_14__ = __webpack_require__(/*! @mui/material/TableCell */ "./node_modules/@mui/material/esm/TableCell/TableCell.js");
/* harmony import */ var _mui_material_TablePagination__WEBPACK_IMPORTED_MODULE_13__ = __webpack_require__(/*! @mui/material/TablePagination */ "./node_modules/@mui/material/esm/TablePagination/TablePagination.js");
/* harmony import */ var _mui_material_Paper__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! @mui/material/Paper */ "./node_modules/@mui/material/esm/Paper/Paper.js");
/* eslint-disable @typescript-eslint/no-unused-vars */


















const PAGE_SIZE = 25;
function NotebookJobsListBody(props) {
    const [notebookJobs, setNotebookJobs] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)(undefined);
    const [jobsQuery, setJobsQuery] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)({});
    const [deletedRows, setDeletedRows] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)(new Set());
    const [page, setPage] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)(0);
    const [maxPage, setMaxPage] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)(0);
    const [loading, setLoading] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)(false);
    const theme = (0,_mui_material_styles__WEBPACK_IMPORTED_MODULE_2__["default"])();
    // Cache environment list — we need this for the output formats.
    const [environmentList, setEnvironmentList] = (0,react__WEBPACK_IMPORTED_MODULE_0__.useState)([]);
    const api = new _handler__WEBPACK_IMPORTED_MODULE_3__.SchedulerService({});
    // Retrieve the environment list once.
    (0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)(() => {
        const setList = async () => {
            setEnvironmentList(await api.getRuntimeEnvironments());
        };
        setList();
    }, []);
    const deleteRow = (0,react__WEBPACK_IMPORTED_MODULE_0__.useCallback)((id) => {
        setDeletedRows(deletedRows => new Set([...deletedRows, id]));
    }, []);
    const fetchInitialRows = async () => {
        // reset pagination state
        setPage(0);
        setMaxPage(0);
        // Get initial job list (next_token is undefined)
        setLoading(true);
        const initialNotebookJobs = await props.getJobs(jobsQuery);
        setLoading(false);
        setNotebookJobs(initialNotebookJobs);
    };
    // Fetch the initial rows asynchronously on component creation
    // After setJobsQuery is called, force a reload.
    (0,react__WEBPACK_IMPORTED_MODULE_0__.useEffect)(() => {
        fetchInitialRows();
    }, [jobsQuery]);
    const fetchMoreRows = async (next_token) => {
        // Do nothing if the next token is undefined (shouldn't happen, but required for type safety)
        if (next_token === undefined) {
            return;
        }
        // Apply the custom token to the existing query parameters
        setLoading(true);
        const newNotebookJobs = await props.getJobs(Object.assign(Object.assign({}, jobsQuery), { next_token }));
        setLoading(false);
        if (!newNotebookJobs) {
            return;
        }
        // Merge the two lists of jobs and keep the next token from the new response.
        setNotebookJobs({
            jobs: [...((notebookJobs === null || notebookJobs === void 0 ? void 0 : notebookJobs.jobs) || []), ...((newNotebookJobs === null || newNotebookJobs === void 0 ? void 0 : newNotebookJobs.jobs) || [])],
            next_token: newNotebookJobs.next_token,
            total_count: newNotebookJobs.total_count
        });
    };
    const trans = (0,_hooks__WEBPACK_IMPORTED_MODULE_4__.useTranslator)('jupyterlab');
    const reloadButton = (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_components_cluster__WEBPACK_IMPORTED_MODULE_5__.Cluster, { justifyContent: "flex-end" },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material_Button__WEBPACK_IMPORTED_MODULE_6__["default"], { variant: "contained", size: "small", onClick: () => fetchInitialRows() }, trans.__('Reload'))));
    const translateStatus = (0,react__WEBPACK_IMPORTED_MODULE_0__.useCallback)((status) => {
        // This may look inefficient, but it's intended to call the `trans` function
        // with distinct, static values, so that code analyzers can pick up all the
        // needed source strings.
        switch (status) {
            case 'CREATED':
                return trans.__('Created');
            case 'QUEUED':
                return trans.__('Queued');
            case 'COMPLETED':
                return trans.__('Completed');
            case 'FAILED':
                return trans.__('Failed');
            case 'IN_PROGRESS':
                return trans.__('In progress');
            case 'STOPPED':
                return trans.__('Stopped');
            case 'STOPPING':
                return trans.__('Stopping');
        }
    }, [trans]);
    if (notebookJobs === undefined) {
        return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("p", null,
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("em", null, trans.__('Loading …'))));
    }
    if (!(notebookJobs === null || notebookJobs === void 0 ? void 0 : notebookJobs.jobs.length)) {
        return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement((react__WEBPACK_IMPORTED_MODULE_0___default().Fragment), null,
            reloadButton,
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("p", { className: 'jp-notebook-job-list-empty' }, trans.__('There are no notebook jobs. ' +
                'Right-click on a file in the file browser to run or schedule a notebook as a job.'))));
    }
    // Display column headers with sort indicators.
    const columns = [
        {
            sortField: 'name',
            name: trans.__('Job name')
        },
        {
            sortField: 'input_uri',
            name: trans.__('Input file')
        },
        {
            sortField: null,
            name: trans.__('Output files')
        },
        {
            sortField: 'create_time',
            name: trans.__('Created at')
        },
        {
            sortField: 'status',
            name: trans.__('Status')
        },
        {
            sortField: null,
            name: trans.__('Actions')
        }
    ];
    const rows = notebookJobs.jobs
        .slice(page * PAGE_SIZE, (page + 1) * PAGE_SIZE)
        .filter(job => !deletedRows.has(job.job_id))
        .map(job => (0,_components_job_row__WEBPACK_IMPORTED_MODULE_7__.buildTableRow)(job, environmentList, props.app, props.showCreateJob, deleteRow, translateStatus, props.showDetailView));
    const handlePageChange = async (e, newPage) => {
        // if newPage <= maxPage, no need to fetch more rows
        if (newPage <= maxPage) {
            setPage(newPage);
            return;
        }
        await fetchMoreRows(notebookJobs.next_token);
        setPage(newPage);
        setMaxPage(newPage);
    };
    // note that the parent must be a JSX fragment for DataGrid to be sized properly
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement((react__WEBPACK_IMPORTED_MODULE_0___default().Fragment), null,
        reloadButton,
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", { style: { flex: 1, height: 0 } },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material_TableContainer__WEBPACK_IMPORTED_MODULE_8__["default"], { component: _mui_material_Paper__WEBPACK_IMPORTED_MODULE_9__["default"], sx: Object.assign({ height: '100%' }, (loading ? { pointerEvents: 'none', opacity: 0.5 } : {})) },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material_Table__WEBPACK_IMPORTED_MODULE_10__["default"], { stickyHeader: true },
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material_TableHead__WEBPACK_IMPORTED_MODULE_11__["default"], null, columns.map((column, idx) => (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(NotebookJobsColumnHeader, { key: idx, gridColumn: column, jobsQuery: jobsQuery, setJobsQuery: setJobsQuery })))),
                    react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material_TableBody__WEBPACK_IMPORTED_MODULE_12__["default"], null, rows)),
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material_TablePagination__WEBPACK_IMPORTED_MODULE_13__["default"], { component: "div", sx: {
                        position: 'sticky',
                        bottom: 0,
                        backgroundColor: theme.palette.background.paper,
                        borderTop: `1px solid ${theme.palette.divider}`
                    }, count: notebookJobs.total_count, page: page, onPageChange: handlePageChange, nextIconButtonProps: {
                        disabled: page === maxPage && !notebookJobs.next_token
                    }, rowsPerPage: PAGE_SIZE, rowsPerPageOptions: [PAGE_SIZE] })))));
}
const sortAscendingIcon = (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.LabIcon.resolveReact, { icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.caretUpIcon, tag: "span" }));
const sortDescendingIcon = (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.LabIcon.resolveReact, { icon: _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.caretDownIcon, tag: "span" }));
function NotebookJobsColumnHeader(props) {
    const sort = props.jobsQuery.sort_by;
    const defaultSort = sort === null || sort === void 0 ? void 0 : sort[0];
    const headerIsDefaultSort = defaultSort && defaultSort.name === props.gridColumn.sortField;
    const isSortedAscending = headerIsDefaultSort &&
        defaultSort &&
        defaultSort.direction === _handler__WEBPACK_IMPORTED_MODULE_3__.Scheduler.SortDirection.ASC;
    const isSortedDescending = headerIsDefaultSort &&
        defaultSort &&
        defaultSort.direction === _handler__WEBPACK_IMPORTED_MODULE_3__.Scheduler.SortDirection.DESC;
    const sortByThisColumn = () => {
        // If this field is not sortable, do nothing.
        if (!props.gridColumn.sortField) {
            return;
        }
        // Change the sort of this column.
        // If not sorted at all or if sorted descending, sort ascending. If sorted ascending, sort descending.
        const newSortDirection = isSortedAscending
            ? _handler__WEBPACK_IMPORTED_MODULE_3__.Scheduler.SortDirection.DESC
            : _handler__WEBPACK_IMPORTED_MODULE_3__.Scheduler.SortDirection.ASC;
        // Set the new sort direction.
        const newSort = {
            name: props.gridColumn.sortField,
            direction: newSortDirection
        };
        // If this field is already present in the sort list, remove it.
        const oldSortList = sort || [];
        const newSortList = [
            newSort,
            ...oldSortList.filter(item => item.name !== props.gridColumn.sortField)
        ];
        // Sub the new sort list in to the query.
        props.setJobsQuery(Object.assign(Object.assign({}, props.jobsQuery), { sort_by: newSortList }));
    };
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material_TableCell__WEBPACK_IMPORTED_MODULE_14__["default"], { onClick: sortByThisColumn, sx: props.gridColumn.sortField ? { cursor: 'pointer' } : {} },
        props.gridColumn.name,
        isSortedAscending && sortAscendingIcon,
        isSortedDescending && sortDescendingIcon));
}
function getJobs(jobQuery) {
    const api = new _handler__WEBPACK_IMPORTED_MODULE_3__.SchedulerService({});
    // Impose max_items if not otherwise specified.
    if (jobQuery['max_items'] === undefined) {
        jobQuery.max_items = PAGE_SIZE;
    }
    return api.getJobs(jobQuery);
}
function NotebookJobsList(props) {
    const trans = (0,_hooks__WEBPACK_IMPORTED_MODULE_4__.useTranslator)('jupyterlab');
    // Retrieve the initial jobs list
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_system_Box__WEBPACK_IMPORTED_MODULE_15__["default"], { sx: { p: 4 }, style: { height: '100%', boxSizing: 'border-box' } },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_system_Stack__WEBPACK_IMPORTED_MODULE_16__["default"], { spacing: 3, style: { height: '100%' } },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_components_heading__WEBPACK_IMPORTED_MODULE_17__.Heading, { level: 1 }, trans.__('Notebook Jobs')),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(NotebookJobsListBody, { showHeaders: true, app: props.app, showCreateJob: props.showCreateJob, getJobs: getJobs, showDetailView: props.showDetailView }))));
}


/***/ }),

/***/ "./lib/model.js":
/*!**********************!*\
  !*** ./lib/model.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "JobsModel": () => (/* binding */ JobsModel),
/* harmony export */   "NotebookJobsListingModel": () => (/* binding */ NotebookJobsListingModel),
/* harmony export */   "convertDescribeJobtoJobDetail": () => (/* binding */ convertDescribeJobtoJobDetail)
/* harmony export */ });
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);


class NotebookJobsListingModel {
    constructor(scheduled_jobs, next_token) {
        const inProgressJobs = scheduled_jobs
            ? scheduled_jobs.filter(job => job.status === 'IN_PROGRESS')
            : [];
        this.inProgressJobCount = inProgressJobs.length;
        this._scheduled_jobs = scheduled_jobs;
        this.scheduledJobsChanged = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_0__.Signal(this);
        this.inProgressJobCountChanged = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_0__.Signal(this);
    }
    updateJobs(jobs) {
        let jobsChanged = false;
        if (jobs.length !== this._scheduled_jobs.length) {
            jobsChanged = true;
        }
        if (!jobsChanged) {
            for (let i = 0; i < jobs.length; i++) {
                const job = jobs[i];
                const modelJob = this._scheduled_jobs[i];
                if (job.status !== modelJob.status) {
                    jobsChanged = true;
                    break;
                }
            }
        }
        if (jobsChanged) {
            this._scheduled_jobs = jobs;
            this.scheduledJobsChanged.emit(jobs);
        }
    }
    updatejobCount(jobCount) {
        if (jobCount !== this.inProgressJobCount) {
            this.inProgressJobCount = jobCount;
            this.inProgressJobCountChanged.emit(jobCount);
        }
    }
}
// Convert an IDescribeJobModel to an IJobDetailModel
function convertDescribeJobtoJobDetail(dj) {
    var _a, _b;
    // Convert parameters
    const jdParameters = Object.entries((_a = dj.parameters) !== null && _a !== void 0 ? _a : {}).map(([pName, pValue]) => {
        return {
            name: pName,
            value: pValue
        };
    });
    // TODO: Convert outputFormats
    return {
        jobId: dj.job_id,
        jobName: (_b = dj.name) !== null && _b !== void 0 ? _b : '',
        inputFile: dj.input_uri,
        outputPath: dj.output_uri,
        outputPrefix: dj.output_prefix,
        environment: dj.runtime_environment_name,
        parameters: jdParameters,
        outputFormats: [],
        computeType: dj.compute_type,
        idempotencyToken: dj.idempotency_token,
        tags: dj.tags,
        status: dj.status,
        createTime: dj.create_time,
        updateTime: dj.update_time,
        startTime: dj.start_time,
        endTime: dj.end_time
    };
}
class JobsModel extends _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.VDomModel {
    constructor(options) {
        super();
        this._jobsView = 'ListJobs';
        this._jobsView = options.jobsView || 'ListJobs';
        this._createJobModel = options.createJobModel || Private.emptyCreateModel();
        this._listJobsModel = options.listJobsModel || { listJobsView: 'Job' };
        this._jobDetailModel = options.jobDetailModel || Object.assign(Object.assign({}, Private.emptyCreateModel()), { jobId: '' });
        this._onModelUpdate = options.onModelUpdate;
        this._jobCount = 0;
    }
    get jobsView() {
        return this._jobsView;
    }
    set jobsView(view) {
        this._jobsView = view;
        this.stateChanged.emit(void 0);
    }
    get createJobModel() {
        return this._createJobModel;
    }
    set createJobModel(model) {
        var _a;
        this._createJobModel = model;
        (_a = this._onModelUpdate) === null || _a === void 0 ? void 0 : _a.call(this);
        this.stateChanged.emit(void 0);
    }
    get listJobsModel() {
        return this._listJobsModel;
    }
    set listJobsModel(model) {
        var _a;
        this._listJobsModel = model;
        (_a = this._onModelUpdate) === null || _a === void 0 ? void 0 : _a.call(this);
        this.stateChanged.emit(void 0);
    }
    get jobDetailModel() {
        return this._jobDetailModel;
    }
    set jobDetailModel(model) {
        var _a;
        this._jobDetailModel = model;
        (_a = this._onModelUpdate) === null || _a === void 0 ? void 0 : _a.call(this);
        this.stateChanged.emit(void 0);
    }
    get jobCount() {
        return this._jobCount;
    }
    set jobCount(count) {
        this._jobCount = count;
    }
}
var Private;
(function (Private) {
    function emptyCreateModel() {
        return {
            jobName: '',
            inputFile: '',
            outputPath: '',
            environment: ''
        };
    }
    Private.emptyCreateModel = emptyCreateModel;
})(Private || (Private = {}));


/***/ }),

/***/ "./lib/notebook-jobs-panel.js":
/*!************************************!*\
  !*** ./lib/notebook-jobs-panel.js ***!
  \************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "NotebookJobsPanel": () => (/* binding */ NotebookJobsPanel)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _mui_material_styles__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @mui/material/styles */ "webpack/sharing/consume/default/@mui/system/@mui/system");
/* harmony import */ var _mui_material_styles__WEBPACK_IMPORTED_MODULE_4___default = /*#__PURE__*/__webpack_require__.n(_mui_material_styles__WEBPACK_IMPORTED_MODULE_4__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _components_icons__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./components/icons */ "./lib/components/icons.js");
/* harmony import */ var _context__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./context */ "./lib/context.js");
/* harmony import */ var _mainviews_create_job__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ./mainviews/create-job */ "./lib/mainviews/create-job.js");
/* harmony import */ var _mainviews_list_jobs__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ./mainviews/list-jobs */ "./lib/mainviews/list-jobs.js");
/* harmony import */ var _mainviews_job_detail__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! ./mainviews/job-detail */ "./lib/mainviews/job-detail.js");
/* harmony import */ var _model__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./model */ "./lib/model.js");
/* harmony import */ var _theme_provider__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./theme-provider */ "./lib/theme-provider.js");










class NotebookJobsPanel extends _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.VDomRenderer {
    constructor(options) {
        var _a, _b, _c;
        super(options.model ||
            new _model__WEBPACK_IMPORTED_MODULE_2__.JobsModel({
                onModelUpdate: () => {
                    // allow us to invoke private parent method
                    // eslint-disable-next-line @typescript-eslint/ban-ts-comment
                    // @ts-ignore
                    this.renderDOM();
                }
            }));
        this.addClass('jp-notebook-jobs-panel');
        const trans = options.translator.load('jupyterlab');
        this.title.icon = (_a = options.titleIcon) !== null && _a !== void 0 ? _a : _components_icons__WEBPACK_IMPORTED_MODULE_3__.calendarMonthIcon;
        this.title.caption = (_b = options.title) !== null && _b !== void 0 ? _b : trans.__('Notebook Jobs');
        this._description = (_c = options.description) !== null && _c !== void 0 ? _c : trans.__('Job Runs');
        this._app = options.app;
        this._translator = options.translator;
        this._advancedOptions = options.advancedOptions;
        this.node.setAttribute('role', 'region');
        this.node.setAttribute('aria-label', trans.__('Notebook Jobs'));
    }
    toggleView() {
        if (this.model.jobsView !== 'CreateJob' &&
            this.model.jobsView !== 'ListJobs') {
            return;
        }
        this.model.jobsView =
            this.model.jobsView === 'ListJobs' ? 'CreateJob' : 'ListJobs';
    }
    showDetailView(jobId) {
        this.model.jobsView = 'JobDetail';
        this.model.jobDetailModel.jobId = jobId;
    }
    render() {
        const showCreateJob = (newModel) => {
            this.model.createJobModel = newModel;
            this.model.jobsView = 'CreateJob';
        };
        return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mui_material_styles__WEBPACK_IMPORTED_MODULE_4__.ThemeProvider, { theme: (0,_theme_provider__WEBPACK_IMPORTED_MODULE_5__.getJupyterLabTheme)() },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_context__WEBPACK_IMPORTED_MODULE_6__["default"].Provider, { value: this._translator },
                this.model.jobsView === 'CreateJob' && (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mainviews_create_job__WEBPACK_IMPORTED_MODULE_7__.CreateJob, { model: this.model.createJobModel, handleModelChange: newModel => (this.model.createJobModel = newModel), toggleView: this.toggleView.bind(this), advancedOptions: this._advancedOptions })),
                this.model.jobsView === 'ListJobs' && (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mainviews_list_jobs__WEBPACK_IMPORTED_MODULE_8__.NotebookJobsList, { app: this._app, model: this.model.listJobsModel, handleModelChange: newModel => (this.model.listJobsModel = newModel), showCreateJob: showCreateJob, showDetailView: this.showDetailView.bind(this) })),
                this.model.jobsView === 'JobDetail' && (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_mainviews_job_detail__WEBPACK_IMPORTED_MODULE_9__.JobDetail, { app: this._app, model: this.model.jobDetailModel, handleModelChange: newModel => (this.model.jobDetailModel = newModel), setCreateJobModel: newModel => (this.model.createJobModel = newModel), setView: view => (this.model.jobsView = view), advancedOptions: this._advancedOptions })))));
    }
}


/***/ }),

/***/ "./lib/theme-provider.js":
/*!*******************************!*\
  !*** ./lib/theme-provider.js ***!
  \*******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "getJupyterLabTheme": () => (/* binding */ getJupyterLabTheme)
/* harmony export */ });
/* harmony import */ var _mui_material_styles__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @mui/material/styles */ "./node_modules/@mui/material/esm/styles/createTheme.js");

function getCSSVariable(name) {
    return getComputedStyle(document.body).getPropertyValue(name).trim();
}
function getJupyterLabTheme() {
    const light = document.body.getAttribute('data-jp-theme-light');
    return (0,_mui_material_styles__WEBPACK_IMPORTED_MODULE_0__["default"])({
        spacing: 4,
        components: {
            MuiButton: {
                defaultProps: {
                    size: 'small'
                }
            },
            MuiFilledInput: {
                defaultProps: {
                    margin: 'dense'
                }
            },
            MuiFormControl: {
                defaultProps: {
                    margin: 'dense'
                }
            },
            MuiFormHelperText: {
                defaultProps: {
                    margin: 'dense'
                }
            },
            MuiIconButton: {
                defaultProps: {
                    size: 'small'
                }
            },
            MuiInputBase: {
                defaultProps: {
                    margin: 'dense',
                    size: 'small'
                }
            },
            MuiInputLabel: {
                defaultProps: {
                    margin: 'dense'
                }
            },
            MuiListItem: {
                defaultProps: {
                    dense: true
                }
            },
            MuiOutlinedInput: {
                defaultProps: {
                    margin: 'dense'
                }
            },
            MuiFab: {
                defaultProps: {
                    size: 'small'
                }
            },
            MuiTable: {
                defaultProps: {
                    size: 'small'
                }
            },
            MuiTextField: {
                defaultProps: {
                    margin: 'dense',
                    size: 'small'
                }
            },
            MuiToolbar: {
                defaultProps: {
                    variant: 'dense'
                }
            }
        },
        palette: {
            mode: light === 'true' ? 'light' : 'dark',
            primary: {
                main: getCSSVariable('--jp-brand-color1'),
                light: getCSSVariable('--jp-brand-color2'),
                dark: getCSSVariable('--jp-brand-color0')
            },
            error: {
                main: getCSSVariable('--jp-error-color1'),
                light: getCSSVariable('--jp-error-color2'),
                dark: getCSSVariable('--jp-error-color0')
            },
            warning: {
                main: getCSSVariable('--jp-warn-color1'),
                light: getCSSVariable('--jp-warn-color2'),
                dark: getCSSVariable('--jp-warn-color0')
            },
            success: {
                main: getCSSVariable('--jp-success-color1'),
                light: getCSSVariable('--jp-success-color2'),
                dark: getCSSVariable('--jp-success-color0')
            },
            text: {
                primary: getCSSVariable('--jp-ui-font-color1'),
                secondary: getCSSVariable('--jp-ui-font-color2'),
                disabled: getCSSVariable('--jp-ui-font-color3')
            }
        },
        shape: {
            borderRadius: 2
        },
        typography: {
            fontFamily: getCSSVariable('--jp-ui-font-family'),
            fontSize: 12,
            htmlFontSize: 16,
            button: {
                textTransform: 'capitalize'
            }
        }
    });
}


/***/ }),

/***/ "./lib/tokens.js":
/*!***********************!*\
  !*** ./lib/tokens.js ***!
  \***********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "Scheduler": () => (/* binding */ Scheduler)
/* harmony export */ });
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__);

var Scheduler;
(function (Scheduler) {
    Scheduler.IAdvancedOptions = new _lumino_coreutils__WEBPACK_IMPORTED_MODULE_0__.Token('@jupyterlab/scheduler:IAdvancedOptions');
})(Scheduler || (Scheduler = {}));


/***/ }),

/***/ "./style/icons/calendar-add-on.svg":
/*!*****************************************!*\
  !*** ./style/icons/calendar-add-on.svg ***!
  \*****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 20 20\" height=\"16px\" width=\"16px\">\n  <path fill=\"#0097A7\" d=\"M10 15.833H4.25q-.729 0-1.24-.51-.51-.511-.51-1.24v-9q0-.729.51-1.239.511-.511 1.24-.511H5V1.667h1.75v1.666h4.833V1.667h1.75v1.666h.75q.729 0 1.24.511.51.51.51 1.239v4.959q-.229-.042-.437-.063-.208-.021-.438-.021-.229 0-.437.021-.209.021-.438.063V7.583H4.25v6.5H10q-.042.229-.062.438-.021.208-.021.437 0 .23.021.438.02.208.062.437Zm4.083 2.5v-2.5h-2.5v-1.75h2.5v-2.5h1.75v2.5h2.5v1.75h-2.5v2.5Z\"/>\n</svg>\n");

/***/ }),

/***/ "./style/icons/calendar-month.svg":
/*!****************************************!*\
  !*** ./style/icons/calendar-month.svg ***!
  \****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 18 18\" height=\"16px\" width=\"16px\">\n  <path fill=\"#0097A7\" d=\"M10 12q-.312 0-.531-.219-.219-.219-.219-.531 0-.312.219-.531.219-.219.531-.219.312 0 .531.219.219.219.219.531 0 .312-.219.531Q10.312 12 10 12Zm-3.25 0q-.312 0-.531-.219Q6 11.562 6 11.25q0-.312.219-.531.219-.219.531-.219.312 0 .531.219.219.219.219.531 0 .312-.219.531Q7.062 12 6.75 12Zm6.5 0q-.312 0-.531-.219-.219-.219-.219-.531 0-.312.219-.531.219-.219.531-.219.312 0 .531.219.219.219.219.531 0 .312-.219.531-.219.219-.531.219ZM10 15q-.312 0-.531-.219-.219-.219-.219-.531 0-.312.219-.531.219-.219.531-.219.312 0 .531.219.219.219.219.531 0 .312-.219.531Q10.312 15 10 15Zm-3.25 0q-.312 0-.531-.219Q6 14.562 6 14.25q0-.312.219-.531.219-.219.531-.219.312 0 .531.219.219.219.219.531 0 .312-.219.531Q7.062 15 6.75 15Zm6.5 0q-.312 0-.531-.219-.219-.219-.219-.531 0-.312.219-.531.219-.219.531-.219.312 0 .531.219.219.219.219.531 0 .312-.219.531-.219.219-.531.219ZM4.5 18q-.625 0-1.062-.448Q3 17.104 3 16.5v-11q0-.604.438-1.052Q3.875 4 4.5 4H6V2h1.5v2h5V2H14v2h1.5q.625 0 1.062.448Q17 4.896 17 5.5v11q0 .604-.438 1.052Q16.125 18 15.5 18Zm0-1.5h11V9h-11v7.5Z\"/>\n</svg>\n");

/***/ }),

/***/ "./style/icons/event-note.svg":
/*!************************************!*\
  !*** ./style/icons/event-note.svg ***!
  \************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"48\" width=\"48\">\n  <path fill=\"#0097A7\" d=\"M14 27v-3h20v3Zm0 9v-3h13.95v3Zm-5 8q-1.2 0-2.1-.9Q6 42.2 6 41V10q0-1.2.9-2.1Q7.8 7 9 7h3.25V4h3.25v3h17V4h3.25v3H39q1.2 0 2.1.9.9.9.9 2.1v31q0 1.2-.9 2.1-.9.9-2.1.9Zm0-3h30V19.5H9V41Z\"/>\n</svg>\n");

/***/ }),

/***/ "./style/icons/replay.svg":
/*!********************************!*\
  !*** ./style/icons/replay.svg ***!
  \********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 22 22\" height=\"16px\" width=\"16px\">\n  <path class=\"jp-icon3\" fill=\"#616161\" d=\"M10 18.125q-1.458 0-2.729-.552-1.271-.552-2.219-1.5t-1.5-2.219Q3 12.583 3 11.125h1.5q0 2.271 1.615 3.885Q7.729 16.625 10 16.625t3.885-1.615q1.615-1.614 1.615-3.885T13.885 7.24Q12.271 5.625 10 5.625h-.125l1.063 1.063L9.875 7.75 7 4.875 9.875 2l1.063 1.062-1.084 1.063H10q1.458 0 2.729.552 1.271.552 2.219 1.5t1.5 2.219Q17 9.667 17 11.125q0 1.458-.552 2.729-.552 1.271-1.5 2.219t-2.219 1.5q-1.271.552-2.729.552Z\"/>\n</svg>\n");

/***/ })

}]);
//# sourceMappingURL=lib_components_job-row_js-lib_index_js-lib_mainviews_list-jobs_js-lib_notebook-jobs-panel_js.7a4903f2467d79e6b3db.js.map
"use strict";
(self["webpackChunkworkbench_jupyterlab"] = self["webpackChunkworkbench_jupyterlab"] || []).push([["lib_index_js"],{

/***/ "./lib/constants.js":
/*!**************************!*\
  !*** ./lib/constants.js ***!
  \**************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "kQuartoApp": () => (/* binding */ kQuartoApp),
/* harmony export */   "kServerEndpoint": () => (/* binding */ kServerEndpoint),
/* harmony export */   "kShinyApp": () => (/* binding */ kShinyApp),
/* harmony export */   "kUrlEndpoint": () => (/* binding */ kUrlEndpoint)
/* harmony export */ });
/*
 * constants.ts
 *
 * Copyright (C) 2022 by Posit Software, PBC
 *
 */
// This file shares variables with './workbench_jupyterlab/constants.py'
// Changes made to this file may need to be duplicated there.
// default process names
const kShinyApp = 'Shiny Project';
const kQuartoApp = 'Quarto Project';
// workbench_jupyterlab server extension endpoints
const kServerEndpoint = 'servers';
const kUrlEndpoint = 'url';


/***/ }),

/***/ "./lib/handler.js":
/*!************************!*\
  !*** ./lib/handler.js ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "requestAPI": () => (/* binding */ requestAPI)
/* harmony export */ });
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/coreutils */ "webpack/sharing/consume/default/@jupyterlab/coreutils");
/* harmony import */ var _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/services */ "webpack/sharing/consume/default/@jupyterlab/services");
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__);
/*
 * handler.ts
 *
 * Copyright (C) 2022 by Posit Software, PBC
 *
 */


/**
 * Call the API extension
 *
 * @param endPoint API REST end point for the extension
 * @param init Initial values for the request
 * @returns The response body interpreted as JSON
 */
async function requestAPI(endPoint = '', init = {}) {
    // Make request to Jupyter API
    const settings = _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.makeSettings();
    const requestUrl = _jupyterlab_coreutils__WEBPACK_IMPORTED_MODULE_0__.URLExt.join(settings.baseUrl, 'workbench-jupyterlab', // API Namespace
    endPoint);
    let response;
    response = await _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.makeRequest(requestUrl, init, settings);
    let data = await response.text();
    if (data.length > 0) {
        try {
            data = JSON.parse(data);
        }
        catch (error) {
            console.log('Not a JSON response body.', response);
        }
    }
    if (!response.ok) {
        throw new _jupyterlab_services__WEBPACK_IMPORTED_MODULE_1__.ServerConnection.ResponseError(response, data.message || data);
    }
    return data;
}


/***/ }),

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _images_posit_icon_fullcolor_svg__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ../images/posit-icon-fullcolor.svg */ "./images/posit-icon-fullcolor.svg");
/* harmony import */ var _images_posit_icon_unstyled_svg__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ../images/posit-icon-unstyled.svg */ "./images/posit-icon-unstyled.svg");
/* harmony import */ var _widget__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./widget */ "./lib/widget.js");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/widgets */ "webpack/sharing/consume/default/@lumino/widgets");
/* harmony import */ var _lumino_widgets__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_widgets__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @jupyterlab/services */ "webpack/sharing/consume/default/@jupyterlab/services");
/* harmony import */ var _jupyterlab_services__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_services__WEBPACK_IMPORTED_MODULE_3__);
/*
 * index.ts
 *
 * Copyright (C) 2022 by Posit Software, PBC
 *
 */







let homeUrl = '/home';
const rstudioIcon = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__.LabIcon({
    name: 'workbench_jupyterlab:home-icon',
    svgstr: _images_posit_icon_fullcolor_svg__WEBPACK_IMPORTED_MODULE_4__["default"],
});
const rstudioPanelIcon = new _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_2__.LabIcon({
    name: 'workbench_jupyterlab:panel-icon',
    svgstr: _images_posit_icon_unstyled_svg__WEBPACK_IMPORTED_MODULE_5__["default"],
});
function returnHome() {
    location.assign(homeUrl);
}
function registerCommands(app, palette) {
    var regex = /(s\/[\w]{5}[\w]{8}[\w]{8}\/)/g;
    const settings = _jupyterlab_services__WEBPACK_IMPORTED_MODULE_3__.ServerConnection.makeSettings();
    homeUrl = settings.baseUrl.replace(regex, 'home/');
    // Register command to return to RStudio Workbench home
    const command = 'workbench_jupyterlab:return-home';
    app.commands.addCommand(command, {
        label: 'Return to Posit Workbench Home',
        caption: 'Return to Posit Workbench Home',
        execute: returnHome
    });
    palette.addItem({ command, category: 'Posit Workbench' });
}
function addRStudioIcon(app) {
    // Add RStudio icon that returns the user to home to menu bar
    const rstudio_widget = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_0__.Widget();
    rstudio_widget.id = 'rsw-icon';
    rstudio_widget.node.onclick = returnHome;
    rstudioIcon.element({
        container: rstudio_widget.node,
        justify: 'center',
        margin: '2px 5px 2px 5px',
        height: 'auto',
        width: '20px',
    });
    app.shell.add(rstudio_widget, 'top', { rank: 1 });
}
function addSideBar(app) {
    // Add the RSW side bar widget to the left panel
    const panel = new _lumino_widgets__WEBPACK_IMPORTED_MODULE_0__.Panel();
    panel.id = 'RStudio-Workbench-tab';
    panel.title.icon = rstudioPanelIcon;
    panel.addWidget(new _widget__WEBPACK_IMPORTED_MODULE_6__.RStudioWorkbenchWidget());
    app.shell.add(panel, 'left', { rank: 501 });
}
function activate(app, palette) {
    registerCommands(app, palette);
    addRStudioIcon(app);
    addSideBar(app);
}
const plugin = {
    // Initialization data for the workbench_jupyterlab extension.
    id: 'workbench-jupyterlab',
    autoStart: true,
    requires: [_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ICommandPalette],
    activate: activate,
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ }),

/***/ "./lib/proxiedServersComponent.js":
/*!****************************************!*\
  !*** ./lib/proxiedServersComponent.js ***!
  \****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "ProxiedServersComponent": () => (/* binding */ ProxiedServersComponent),
/* harmony export */   "Server": () => (/* binding */ Server)
/* harmony export */ });
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/ui-components */ "webpack/sharing/consume/default/@jupyterlab/ui-components");
/* harmony import */ var _jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__);
/*
 * proxiedServersComponent.tsx
 *
 * Copyright (C) 2022 by Posit Software, PBC
 *
 */
// This file shares variables with './workbench_jupyterlab/constants.py'


const TitleComponent = (props) => {
    const headerId = ('title_component_' + props.title).replace(/\s+/g, '_');
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", null,
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("header", { id: headerId }, props.title)));
};
const ServerComponent = (props) => {
    const hyperlinkId = 'server_link_' + props.server.html_id;
    const liId = 'server_component_' + props.server.html_id;
    const serverNameId = 'server_name_' + props.server.html_id;
    const serverInfoId = 'server_info_' + props.server.html_id;
    return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(react__WEBPACK_IMPORTED_MODULE_0__.Fragment, { "aria-role": 'link', "aria-label": 'Open link for proxied server ' + props.server.label },
        react__WEBPACK_IMPORTED_MODULE_0___default().createElement("a", { id: hyperlinkId, target: "_blank", title: props.server.title, href: props.server.securePath },
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("li", { id: liId },
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement(_jupyterlab_ui_components__WEBPACK_IMPORTED_MODULE_1__.launcherIcon.react, { paddingRight: 5 }),
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("span", { id: serverNameId, className: 'jp-ServerName' }, props.server.label),
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("span", { id: serverInfoId, className: 'jp-ServerInfo' },
                    props.server.ip,
                    ":",
                    props.server.port)))));
};
class ProxiedServersComponent extends react__WEBPACK_IMPORTED_MODULE_0__.Component {
    constructor(props) {
        super(props);
    }
    render() {
        const serverItems = this.props.servers.map((server) => react__WEBPACK_IMPORTED_MODULE_0___default().createElement(ServerComponent, { server: server }));
        return (react__WEBPACK_IMPORTED_MODULE_0___default().createElement(react__WEBPACK_IMPORTED_MODULE_0__.Fragment, null,
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement(TitleComponent, { title: 'Proxied Servers' }),
            react__WEBPACK_IMPORTED_MODULE_0___default().createElement("div", null,
                react__WEBPACK_IMPORTED_MODULE_0___default().createElement("ul", { id: 'proxied_servers_list' }, serverItems))));
    }
}
class Server {
    constructor(pid, name, port, ip, securePath) {
        this.pid = pid;
        this.label = name;
        this.port = port;
        this.ip = ip;
        this.securePath = securePath;
        this.title = securePath && securePath != '' ? securePath : 'Could not create secure url.';
        let id_str = this.label + '_' + port;
        id_str = id_str.replace(/\s+|-/g, '_'); // replace spaces with an underscore
        this.html_id = id_str.replace(/_+/g, '_'); // remove any duplicated underscores
    }
}
;


/***/ }),

/***/ "./lib/widget.js":
/*!***********************!*\
  !*** ./lib/widget.js ***!
  \***********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "RStudioWorkbenchWidget": () => (/* binding */ RStudioWorkbenchWidget)
/* harmony export */ });
/* harmony import */ var _constants__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./constants */ "./lib/constants.js");
/* harmony import */ var _handler__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./handler */ "./lib/handler.js");
/* harmony import */ var _proxiedServersComponent__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./proxiedServersComponent */ "./lib/proxiedServersComponent.js");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @lumino/signaling */ "webpack/sharing/consume/default/@lumino/signaling");
/* harmony import */ var _lumino_signaling__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_lumino_signaling__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! react */ "webpack/sharing/consume/default/react");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_2__);
/*
 * widget.tsx
 *
 * Copyright (C) 2022 by Posit Software, PBC
 *
 */
// This file shares variables with './workbench_jupyterlab/constants.py'






function UseSignalComponent(props) {
    return react__WEBPACK_IMPORTED_MODULE_2___default().createElement(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.UseSignal, { signal: props.signal, initialArgs: props.servers }, (_, servers) => react__WEBPACK_IMPORTED_MODULE_2___default().createElement(_proxiedServersComponent__WEBPACK_IMPORTED_MODULE_3__.ProxiedServersComponent, { servers: servers }));
}
class RStudioWorkbenchWidget extends _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_0__.ReactWidget {
    constructor() {
        super();
        this.servers = new Map();
        this._signal = new _lumino_signaling__WEBPACK_IMPORTED_MODULE_1__.Signal(this);
        this._serverString = '';
        this._sessionUrl = '';
        this.addClass('jp-RStudioWorkbenchWidget');
    }
    getSessionUrl() {
        (0,_handler__WEBPACK_IMPORTED_MODULE_4__.requestAPI)(_constants__WEBPACK_IMPORTED_MODULE_5__.kUrlEndpoint).then((response) => {
            try {
                this._sessionUrl = response.baseSessionUrl;
            }
            catch (error) {
                console.log(`Received invalid response on GET /workbench-jupyterlab/url. \n${error}`);
            }
        }, (error) => {
            console.log(`Error on GET /workbench-jupyterlab/url. \n${error}`);
        });
    }
    requestServers() {
        (0,_handler__WEBPACK_IMPORTED_MODULE_4__.requestAPI)(_constants__WEBPACK_IMPORTED_MODULE_5__.kServerEndpoint).then((response) => {
            if (JSON.stringify(response.servers) != this._serverString) {
                this._serverString = JSON.stringify(response.servers);
                this.servers.clear();
                try {
                    response.servers.forEach((server) => {
                        this.servers.set(server.pid, [new _proxiedServersComponent__WEBPACK_IMPORTED_MODULE_3__.Server(server.pid, server.label, server.port, server.ip, `${this._sessionUrl}p/${server.secure_port}/`)]);
                    });
                    this._signal.emit(this.getServers());
                }
                catch (error) {
                    console.log(`Received invalid response on GET /workbench-jupyterlab/servers. \n${response}`);
                    return;
                }
            }
        }, (error) => {
            console.log(`Error on GET /workbench-jupyterlab/servers. \n${error}`);
        });
    }
    async onAfterAttach(msg) {
        super.onAfterAttach(msg);
        this.requestServers();
    }
    async onBeforeShow(msg) {
        super.onBeforeShow(msg);
        this.getSessionUrl();
        this.requestServers();
        this._timerID = setInterval(() => this.requestServers(), 3000);
    }
    onAfterHide(msg) {
        super.onAfterHide(msg);
        clearInterval(this._timerID);
    }
    getServers() {
        let serverArray = [];
        this.servers.forEach((value, key) => {
            serverArray = serverArray.concat(value);
        });
        return serverArray;
    }
    render() {
        return (react__WEBPACK_IMPORTED_MODULE_2___default().createElement(UseSignalComponent, { signal: this._signal, servers: this.getServers() }));
    }
}


/***/ }),

/***/ "./images/posit-icon-fullcolor.svg":
/*!*****************************************!*\
  !*** ./images/posit-icon-fullcolor.svg ***!
  \*****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<!-- Generator: Adobe Illustrator 26.4.1, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->\n<svg version=\"1.1\" id=\"Layer_1\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" x=\"0px\" y=\"0px\"\n\t width=\"184px\" height=\"182.5px\" viewBox=\"0 0 184 182.5\" style=\"enable-background:new 0 0 184 182.5;\" xml:space=\"preserve\">\n<style type=\"text/css\">\n\t.st0{fill:#EE6331;}\n\t.st1{fill:#447099;}\n</style>\n<g id=\"posit-logo\">\n\t<polygon id=\"fullLogo-8\" class=\"st0\" points=\"38,73.1 46.2,69.5 82.9,53.3 90.9,49.7 179.7,10.5 179.7,57.8 143.8,73.1 135.7,69.5 \n\t\t173.2,53.5 173.2,20.5 98.9,53.3 90.9,56.8 54.3,73 46.2,76.6 20.3,88 20.3,96.5 45.8,107.8 53.9,111.4 91.5,128 99.5,131.5 \n\t\t173.2,164.1 173.2,130.7 136.1,114.9 144.2,111.3 179.7,126.4 179.7,174 91.5,135.1 83.6,131.6 45.8,114.9 37.6,111.3 13.8,100.7 \n\t\t13.8,83.8 \t\"/>\n\t<polygon class=\"st0\" points=\"99.2,92.1 135.6,76.6 127.5,73 82.6,92.1 127.9,111.4 136,107.8 \t\"/>\n\t<polygon id=\"fullLogo-9\" class=\"st1\" points=\"45.8,107.8 53.9,111.4 90.9,95.6 82.7,92.1 \t\"/>\n\t<polygon id=\"fullLogo-10\" class=\"st1\" points=\"54.3,73 46.2,76.6 82.7,92.1 90.9,88.6 \t\"/>\n\t<polygon id=\"fullLogo-11\" class=\"st1\" points=\"143.8,73.1 135.7,69.5 98.9,53.3 90.9,49.7 2.1,10.5 2.1,57.8 38,73.1 46.2,69.5 \n\t\t8.6,53.5 8.6,20.5 82.9,53.3 90.9,56.8 127.5,73 135.6,76.6 161.6,88 161.6,96.5 136.1,107.8 127.9,111.4 90.4,128 82.4,131.5 \n\t\t8.6,164.1 8.6,130.7 45.8,114.9 37.6,111.3 2.1,126.4 2.1,174 90.3,135.1 98.3,131.6 136.1,114.9 144.2,111.3 168,100.7 168,83.8 \t\n\t\t\"/>\n</g>\n</svg>\n");

/***/ }),

/***/ "./images/posit-icon-unstyled.svg":
/*!****************************************!*\
  !*** ./images/posit-icon-unstyled.svg ***!
  \****************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = ("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<!-- Generator: Adobe Illustrator 26.4.1, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->\n<svg version=\"1.1\" id=\"Layer_1\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" viewBox=\"0 0 184 182.5\" xml:space=\"preserve\">\n<g id=\"posit-logo\">\n\t<polygon id=\"fullLogo-8\" points=\"38,73.1 46.2,69.5 82.9,53.3 90.9,49.7 179.7,10.5 179.7,57.8 143.8,73.1 135.7,69.5 \n\t\t173.2,53.5 173.2,20.5 98.9,53.3 90.9,56.8 54.3,73 46.2,76.6 20.3,88 20.3,96.5 45.8,107.8 53.9,111.4 91.5,128 99.5,131.5 \n\t\t173.2,164.1 173.2,130.7 136.1,114.9 144.2,111.3 179.7,126.4 179.7,174 91.5,135.1 83.6,131.6 45.8,114.9 37.6,111.3 13.8,100.7 \n\t\t13.8,83.8 \t\"/>\n\t<polygon points=\"99.2,92.1 135.6,76.6 127.5,73 82.6,92.1 127.9,111.4 136,107.8 \t\"/>\n\t<polygon id=\"fullLogo-9\" points=\"45.8,107.8 53.9,111.4 90.9,95.6 82.7,92.1 \t\"/>\n\t<polygon id=\"fullLogo-10\" points=\"54.3,73 46.2,76.6 82.7,92.1 90.9,88.6 \t\"/>\n\t<polygon id=\"fullLogo-11\" points=\"143.8,73.1 135.7,69.5 98.9,53.3 90.9,49.7 2.1,10.5 2.1,57.8 38,73.1 46.2,69.5 \n\t\t8.6,53.5 8.6,20.5 82.9,53.3 90.9,56.8 127.5,73 135.6,76.6 161.6,88 161.6,96.5 136.1,107.8 127.9,111.4 90.4,128 82.4,131.5 \n\t\t8.6,164.1 8.6,130.7 45.8,114.9 37.6,111.3 2.1,126.4 2.1,174 90.3,135.1 98.3,131.6 136.1,114.9 144.2,111.3 168,100.7 168,83.8 \t\n\t\t\"/>\n</g>\n</svg>\n");

/***/ })

}]);
//# sourceMappingURL=lib_index_js.4140eb36ab21d68e5cb6.js.map
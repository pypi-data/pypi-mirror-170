(self["webpackChunkjmv"] = self["webpackChunkjmv"] || []).push([["lib_index_js"],{

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";

// Copyright (c) KaivnD
// Distributed under the terms of the Modified BSD License.
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    Object.defineProperty(o, k2, { enumerable: true, get: function() { return m[k]; } });
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __exportStar = (this && this.__exportStar) || function(m, exports) {
    for (var p in m) if (p !== "default" && !Object.prototype.hasOwnProperty.call(exports, p)) __createBinding(exports, m, p);
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
// (() => {
//   const head = document.querySelector('head');
//   const overrideStyles = document.createElement('style');
//   overrideStyles.innerText = `
//     .cell-output-ipywidget-background {
//       background: none !important;
//     }
//     `;
//   head?.appendChild(overrideStyles);
// })();
__exportStar(__webpack_require__(/*! ./version */ "./lib/version.js"), exports);
__exportStar(__webpack_require__(/*! ./widget */ "./lib/widget.js"), exports);
//# sourceMappingURL=index.js.map

/***/ }),

/***/ "./lib/version.js":
/*!************************!*\
  !*** ./lib/version.js ***!
  \************************/
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {

"use strict";

// Copyright (c) KaivnD
// Distributed under the terms of the Modified BSD License.
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.MODULE_NAME = exports.MODULE_VERSION = void 0;
// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-ignore
// eslint-disable-next-line @typescript-eslint/no-var-requires
const data = __webpack_require__(/*! ../package.json */ "./package.json");
/**
 * The _model_module_version/_view_module_version this package implements.
 *
 * The html widget manager assumes that this is the same as the npm package
 * version number.
 */
exports.MODULE_VERSION = data.version;
/*
 * The current package name.
 */
exports.MODULE_NAME = data.name;
//# sourceMappingURL=version.js.map

/***/ }),

/***/ "./lib/widget.js":
/*!***********************!*\
  !*** ./lib/widget.js ***!
  \***********************/
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {

"use strict";

var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.DisplayPortalView = exports.DisplayPortalModel = void 0;
// Copyright (c) KaivnD
// Distributed under the terms of the Modified BSD License.
const base_1 = __webpack_require__(/*! @jupyter-widgets/base */ "webpack/sharing/consume/default/@jupyter-widgets/base");
const version_1 = __webpack_require__(/*! ./version */ "./lib/version.js");
// Import the CSS
__webpack_require__(/*! ../css/widget.css */ "./css/widget.css");
// import { DisplayPortal } from './components/DisplayPortal';
const _3dp_1 = __importDefault(__webpack_require__(/*! 3dp */ "./node_modules/.pnpm/3dp@0.0.1/node_modules/3dp/dist/3dp.umd.cjs"));
class DisplayPortalModel extends base_1.DOMWidgetModel {
    defaults() {
        return Object.assign(Object.assign({}, super.defaults()), { _model_name: DisplayPortalModel.model_name, _model_module: DisplayPortalModel.model_module, _model_module_version: DisplayPortalModel.model_module_version, _view_name: DisplayPortalModel.view_name, _view_module: DisplayPortalModel.view_module, _view_module_version: DisplayPortalModel.view_module_version, meshbuffers: [], wirebuffers: [], options: {} });
    }
}
exports.DisplayPortalModel = DisplayPortalModel;
DisplayPortalModel.serializers = Object.assign({}, base_1.DOMWidgetModel.serializers);
DisplayPortalModel.model_name = 'DisplayPortalModel';
DisplayPortalModel.model_module = version_1.MODULE_NAME;
DisplayPortalModel.model_module_version = version_1.MODULE_VERSION;
DisplayPortalModel.view_name = 'DisplayPortalView'; // Set to null if no view
DisplayPortalModel.view_module = version_1.MODULE_NAME; // Set to null if no view
DisplayPortalModel.view_module_version = version_1.MODULE_VERSION;
const wiresbuffer = [
    {
        data: [
            8.704402, 23.169317, 0, 12.404402, 23.169317, 0, 12.404402, 21.669317, 0,
            17.004402, 21.669317, 0, 17.004402, 22.869317, 0, 19.004402, 22.869317, 0,
            19.004402, 24.919317, 0, 21.804402, 24.919317, 0, 21.804402, 22.469317, 0,
            24.604402, 22.469317, 0, 24.604402, 17.069317, 0, 24.004402, 17.069317, 0,
            24.004402, 13.969317, 0, 29.004402, 13.969317, 0, 29.004402, 17.069317, 0,
            28.404402, 17.069317, 0, 28.404402, 22.469317, 0, 31.204402, 22.469317, 0,
            31.204402, 24.919317, 0, 34.004402, 24.919317, 0, 34.004402, 22.869317, 0,
            36.004402, 22.869317, 0, 36.004402, 21.669317, 0, 40.604402, 21.669317, 0,
            40.604402, 23.169317, 0, 44.304402, 23.169317, 0, 44.304402, 19.869317, 0,
            45.004402, 19.869317, 0, 45.004402, 18.469317, 0, 45.004402, 18.269317, 0,
            45.004402, 16.669317, 0, 43.804402, 16.669317, 0, 43.804402, 11.119317, 0,
            43.804402, 10.919317, 0, 43.804402, 10.253817, 0, 40.004402, 10.269317, 0,
            40.004402, 11.769317, 0, 36.004402, 11.769317, 0, 36.004402, 9.469317, 0,
            33.504402, 9.469317, 0, 33.504402, 5.533817, 0, 30.004402, 5.533817, 0,
            30.004402, 6.369317, 0, 23.004402, 6.369317, 0, 23.004402, 5.533817, 0,
            19.504402, 5.529817, 0, 19.504402, 9.469317, 0, 17.004402, 9.469317, 0,
            17.004402, 11.769317, 0, 13.004402, 11.769317, 0, 13.004402, 10.269317, 0,
            9.204402, 10.269317, 0, 9.204402, 10.369317, 0, 9.204402, 11.119317, 0,
            9.204402, 16.669317, 0, 8.004402, 16.669317, 0, 8.004402, 18.269317, 0,
            8.004402, 18.469317, 0, 8.004402, 19.869317, 0, 8.704402, 19.869317, 0,
            8.704402, 23.169317, 0,
        ],
    },
];
class DisplayPortalView extends base_1.DOMWidgetView {
    initialize(parameters) {
        const backbone = this;
        const model = this.model;
        const container = document.createElement('div');
        container.style.height = `${model.attributes._height}px`;
        container.style.width = '100%';
        const buffers = [];
        const option = {};
        _3dp_1.default(container, buffers, wiresbuffer, option);
        backbone.el.append(container);
    }
}
exports.DisplayPortalView = DisplayPortalView;
//# sourceMappingURL=widget.js.map

/***/ }),

/***/ "./node_modules/.pnpm/css-loader@3.6.0_webpack@5.74.0/node_modules/css-loader/dist/cjs.js!./css/widget.css":
/*!*****************************************************************************************************************!*\
  !*** ./node_modules/.pnpm/css-loader@3.6.0_webpack@5.74.0/node_modules/css-loader/dist/cjs.js!./css/widget.css ***!
  \*****************************************************************************************************************/
/***/ ((module, exports, __webpack_require__) => {

// Imports
var ___CSS_LOADER_API_IMPORT___ = __webpack_require__(/*! ../node_modules/.pnpm/css-loader@3.6.0_webpack@5.74.0/node_modules/css-loader/dist/runtime/api.js */ "./node_modules/.pnpm/css-loader@3.6.0_webpack@5.74.0/node_modules/css-loader/dist/runtime/api.js");
exports = ___CSS_LOADER_API_IMPORT___(false);
// Module
exports.push([module.id, ".custom-widget {\n  background-color: lightseagreen;\n  padding: 0px 2px;\n}\n.cell-output-ipywidget-background {\n  background: none !important;\n}", ""]);
// Exports
module.exports = exports;


/***/ }),

/***/ "./css/widget.css":
/*!************************!*\
  !*** ./css/widget.css ***!
  \************************/
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var api = __webpack_require__(/*! !../node_modules/.pnpm/style-loader@1.3.0_webpack@5.74.0/node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js */ "./node_modules/.pnpm/style-loader@1.3.0_webpack@5.74.0/node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js");
            var content = __webpack_require__(/*! !!../node_modules/.pnpm/css-loader@3.6.0_webpack@5.74.0/node_modules/css-loader/dist/cjs.js!./widget.css */ "./node_modules/.pnpm/css-loader@3.6.0_webpack@5.74.0/node_modules/css-loader/dist/cjs.js!./css/widget.css");

            content = content.__esModule ? content.default : content;

            if (typeof content === 'string') {
              content = [[module.id, content, '']];
            }

var options = {};

options.insert = "head";
options.singleton = false;

var update = api(content, options);



module.exports = content.locals || {};

/***/ }),

/***/ "./package.json":
/*!**********************!*\
  !*** ./package.json ***!
  \**********************/
/***/ ((module) => {

"use strict";
module.exports = JSON.parse('{"name":"jmv","version":"0.1.0","description":"jupyter moon view","keywords":["jupyter","jupyterlab","jupyterlab-extension","widgets"],"files":["lib/**/*.js","dist/*.js","css/*.css"],"homepage":"https://github.com/KaivnD/jmv","bugs":{"url":"https://github.com/KaivnD/jmv/issues"},"license":"BSD-3-Clause","author":{"name":"KaivnD","email":"KaivnD@hotmail.com"},"main":"lib/index.js","types":"./lib/index.d.ts","repository":{"type":"git","url":"https://github.com/KaivnD/jmv"},"scripts":{"build":"pnpm run build:lib && pnpm run build:nbextension && pnpm run build:labextension:dev","build:prod":"pnpm run build:lib && pnpm run build:nbextension && pnpm run build:labextension","build:labextension":"jupyter labextension build .","build:labextension:dev":"jupyter labextension build --development True .","build:lib":"tsc","build:nbextension":"webpack","clean":"pnpm run clean:lib && pnpm run clean:nbextension && pnpm run clean:labextension","clean:lib":"rimraf lib","clean:labextension":"rimraf jmv/labextension","clean:nbextension":"rimraf jmv/nbextension/static/index.js","lint":"eslint . --ext .ts,.tsx --fix","lint:check":"eslint . --ext .ts,.tsx","prepack":"pnpm run build:lib","test":"jest","watch":"npm-run-all -p watch:*","watch:lib":"tsc -w","watch:nbextension":"webpack --watch --mode=development","watch:labextension":"jupyter labextension watch ."},"dependencies":{"@jupyter-widgets/base":"^1.1.10 || ^2.0.0 || ^3.0.0 || ^4.0.0"},"devDependencies":{"3dp":"^0.0.1","@babel/core":"^7.5.0","@babel/preset-env":"^7.5.0","@jupyterlab/builder":"^3.0.0","@phosphor/application":"^1.6.0","@phosphor/widgets":"^1.6.0","@types/jest":"^26.0.24","@types/webpack-env":"^1.13.6","@typescript-eslint/eslint-plugin":"^3.6.0","@typescript-eslint/parser":"^3.6.0","acorn":"^7.2.0","crypto":"1.0.1","css-loader":"^3.2.0","eslint":"^7.4.0","eslint-config-prettier":"^6.11.0","eslint-plugin-prettier":"^3.1.4","fs-extra":"^7.0.0","htm":"^3.1.1","identity-obj-proxy":"^3.0.0","jest":"^26.0.0","mkdirp":"^0.5.1","npm-run-all":"^4.1.3","prettier":"^2.0.5","rimraf":"^2.6.2","source-map-loader":"^1.1.3","style-loader":"^1.0.0","ts-jest":"^26.0.0","ts-loader":"^8.0.0","typescript":"~4.1.3","webpack":"^5.61.0","webpack-cli":"^4.0.0"},"jupyterlab":{"extension":"lib/plugin","outputDir":"jmv/labextension/","sharedPackages":{"@jupyter-widgets/base":{"bundled":false,"singleton":true}}}}');

/***/ })

}]);
//# sourceMappingURL=lib_index_js.b25f4ec1da9b47356161.js.map
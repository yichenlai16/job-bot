import { createApp } from "vue";
import Vant from "vant";
import "vant/lib/index.css";
import App from "./App.vue";

import Descriptions from "ant-design-vue/lib/descriptions";
import "ant-design-vue/lib/descriptions/style/index.css";

import Drawer from "ant-design-vue/lib/drawer";
import "ant-design-vue/lib/drawer/style/index.css";

import Card from "ant-design-vue/lib/card";
import "ant-design-vue/lib/card/style/index.css";

import Grid from "ant-design-vue/lib/grid";
import "ant-design-vue/lib/grid/style/index.css";

import Space from "ant-design-vue/lib/space";
import "ant-design-vue/lib/space/style/index.css";

import Modal from "ant-design-vue/lib/modal";
import "ant-design-vue/lib/modal/style/index.css";

import Table from "ant-design-vue/lib/table";
import "ant-design-vue/lib/table/style/index.css";

import Statistic from "ant-design-vue/lib/statistic";
import "ant-design-vue/lib/statistic/style/index.css";

import { Row, Col } from "ant-design-vue/lib/grid";

const app = createApp(App).use(router);

// Vant框架
app.use(Vant);

app.use(Descriptions);
app.use(Drawer);
app.use(Col);
app.use(Row);
app.use(Card);
app.use(Grid);
app.use(Statistic);
app.use(Space);
app.use(Modal);
app.use(Table);
import { Locale } from "vant";
import zhTW from "vant/es/locale/lang/zh-TW";

Locale.use("zh-TW", zhTW);

// VueRouter模組
// import Vue from "vue";
// import VueRouter from "vue-router";
import router from "./router";
app.use(router);

URLSearchParams.prototype.appendIfExists = function (key, value) {
  if (value !== null && value !== undefined) {
    this.append(key, value);
  }
};

app.mount("#app");

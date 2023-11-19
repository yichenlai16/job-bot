import { createRouter, createWebHistory } from "vue-router";
import Main from "@/views/Main.vue";
// import qs from "qs";
const routes = [
  // {
  //   path: "/",
  //   component: () => import("../views/Redirect.vue"),
  // },
  {
    path: "/",
    component: Main,
  },
  {
    path: "/main",
    name: "Main",
    component: Main,
  },
  {
    path: "/search",
    name: "SearchResults",
    component: () => import("../views/Search/SearchResults.vue"),
  },
  {
    path: "/about",
    name: "About",
    component: () => import("../views/About.vue"),
  },
  {
    path: "/job/:id",
    name: "Job",
    component: () => import("../views/JobDetail.vue"),
  },
  {
    path: "/company/:id",
    name: "Company",
    component: () => import("../views/CompanyDetail.vue"),
  },
  {
    path: "/alert",
    name: "Alert",
    component: () => import("../views/Alert.vue"),
  },
  {
    path: "/alert/:id",
    name: "AlertDetail",
    component: () => import("../views/AlertDetail.vue"),
  },
  {
    path: "/alertpost",
    name: "AddAlert",
    component: () => import("../views/Alert/PostAlert.vue"),
  },
  {
    path: "/alertredirect/:id",
    name: "AlertRedirect",
    component: () => import("../views/AlertRedirect.vue"),
  },
  {
    path: "/line",
    name: "Line",
    component: () => import("../views/Line.vue"),
  },
  {
    path: "/line/auth",
    name: "LineLogin",
    component: () => import("../views/LineLogin.vue"),
  },
  {
    path: "/notify/callback",
    name: "NotifyCallback",
    component: () => import("../views/Notify/Callback.vue"),
  },
  {
    path: "/callback",
    name: "Callback",
    component: () => import("../views/Notify/Callback.vue"),
  },
  {
    path: "/redirect",
    name: "Redirect",
    component: () => import("../views/Redirect.vue"),
  },
  {
    path: "/admin",
    name: "Admin",
    component: () => import("../views/Admin.vue"),
  },
  {
    path: "/:pathMatch(.*)",
    component: () => import("../components/NotFoundComponent.vue"),
  },
];

const router = createRouter({
  history: createWebHistory("/"),
  routes,
});

export default router;

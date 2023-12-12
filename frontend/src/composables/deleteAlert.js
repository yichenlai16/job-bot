import axios from "axios";
import getCookie from "@/composables/getCookie.js";
// import {router} from "vue-router";
export default function deleteAlert(key) {
  axios
    .delete("/api/alert/" + key + "/", {
      headers: {
        "X-CSRFToken": getCookie("csrftoken"),
      },
    })
    .then(function () {
      history.go(0);
    });
}

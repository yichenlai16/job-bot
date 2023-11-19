import { onMounted, watch } from "vue";
import liff from "@line/liff";
export default function getUserData(info, route) {
  const getData = async () => {
    liff.init({ liffId: "1656495409-YPJpOrV4" });
    const response = await liff.getProfile();
    info.value = response;
  };

  onMounted(() => {
    getData();
  });
  watch(route, getData);
}

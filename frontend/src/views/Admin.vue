<template>
  <topBar />

  <a-table 
  :dataSource="dataSource" 
  :columns="columns"
  bordered = true
  size = "small" />
</template>

<script>
import topBar from "@/components/Navigation/TopBar";
export default {
  name: "Admin",
  components: {
    topBar,
  },
  setup() {
    return {
      dataSource: [
        {
          id: 15,
          user: {
            id: 1,
            name: "辰",
            notify_token: "b7uwdUKGZr9LlZTOSNkBRxYWQdKsL2P3aOOcx5AqJia",
          },
          title: "台北市大安區全部",
          keyword: "",
          area: "台北市大安區",
          cat: "",
          period: "",
          salary: null,
        },
        {
          id: 17,
          user: {
            id: 1,
            name: "辰",
            notify_token: "b7uwdUKGZr9LlZTOSNkBRxYWQdKsL2P3aOOcx5AqJia",
          },
          title: "台北市的專員",
          keyword: "專員",
          area: "台北市",
          cat: "",
          period: "",
          salary: null,
        },
        {
          id: 18,
          user: {
            id: 1,
            name: "辰",
            notify_token: "b7uwdUKGZr9LlZTOSNkBRxYWQdKsL2P3aOOcx5AqJia",
          },
          title: "專員",
          keyword: "專員",
          area: "",
          cat: "",
          period: "",
          salary: null,
        },
        {
          id: 19,
          user: {
            id: 1,
            name: "辰",
            notify_token: "b7uwdUKGZr9LlZTOSNkBRxYWQdKsL2P3aOOcx5AqJia",
          },
          title: "台北市助理",
          keyword: "助理",
          area: "",
          cat: "",
          period: "",
          salary: null,
        },
        {
          id: 21,
          user: {
            id: 2,
            name: "林庭安",
            notify_token: "uVruDPMnNhXEiLxbqtFajuOPZkfJ1Gjpp0Rh4gwA1wW",
          },
          title: "新職缺",
          keyword: "",
          area: "台北市",
          cat: "餐飲服務生,調酒師╱吧台人員,",
          period: "假日班",
          salary: null,
        },
      ],

      columns: [
        {
          title: "提醒ID",
          dataIndex: ["id"],
          key: ["id"],
        },
        {
          title: "userID",
          dataIndex: ["user", "id"],
          key: ["user", "id"],
        },
        {
          title: "username",
          dataIndex: ["user", "name"],
          key: ["user", "name"],
        },
        {
          title: "提醒名字",
          dataIndex: "title",
          key: "title",
        },
        {
          title: "條件:關鍵字",
          dataIndex: "keyword",
          key: "keyword",
        },
        {
          title: "條件:地區",
          dataIndex: "area",
          key: "area",
        },
        {
          title: "條件:類別",
          dataIndex: "cat",
          key: "cat",
        },
      ],
    };
  },
};
</script>

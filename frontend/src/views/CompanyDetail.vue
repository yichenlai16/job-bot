<template>
  <TopBarClickLeft />

  <div
    class="van-hairline--top-bottom van-safe-area-bottom"
    v-if="company !== null"
  >
    <van-cell-group title="公司資料" inset>
      <van-cell>
        <template #value>
          <h3>
            {{ company.name }}
          </h3>
        </template>
      </van-cell>

      <van-cell>
        <template #value>
          <h3>
            {{ company.area }}
          </h3>
        </template>
      </van-cell>
    </van-cell-group>

    <van-cell-group title="公司介紹">
      <van-cell>
        <template #value>產業類別：{{ company.category }} </template>
      </van-cell>
      <van-cell>
        <template #value>產業描述：{{ company.categoryDesc }} </template>
      </van-cell>
      <van-cell>
        <template #value>資本額：{{ company.capital }} </template>
      </van-cell>
      <van-cell>
        <template #value>聯絡人：{{ company.contactPerson }} </template>
      </van-cell>
      <van-cell>
        <template #value>電話：{{ company.phone }} </template>
      </van-cell>
      <van-cell>
        <template #value>傳真：{{ company.fax }} </template>
      </van-cell>
      <van-cell>
        <template #value>員工人數：{{ company.empNo }} </template>
      </van-cell>
      <van-cell>
        <template #value>地址：{{ company.address }} </template>
      </van-cell>
      <van-cell v-if="company.coLink !== ''">
        <template #value>網站：{{ company.link }} </template>
      </van-cell>
      <van-cell>
        <template #value>
          <div class="text-block van-multi-ellipsis--l2">
            {{ company.companyProfile }}
          </div>
          <van-button type="default" @click="extendText()" v-show="isShow" block
            >更多
          </van-button>
        </template>
      </van-cell>
    </van-cell-group>

    <van-cell-group title="主要商品／服務項目">
      <van-cell v-if="company.coProduct !== ''">
        <template #value>
          <div class="text-block van-multi-ellipsis--l2">
            {{ company.product }}
          </div>
          <van-button type="default" @click="extendText()" v-show="isShow" block
            >更多
          </van-button>
        </template>
      </van-cell>

      <van-cell v-if="company.product == ''" value="暫不提供"></van-cell>
    </van-cell-group>
    <van-cell-group title="相關職缺">
      <div
        v-for="job in company.job"
        v-bind:key="job.id"
        @click="showDrawer(job)"
      >
        <van-cell is-link>
          <template #title class="jobName">
            <div class="van-ellipsis">{{ job.name }}</div>
          </template>
          <template #label class="companyName">{{ job.company_name }}</template>
        </van-cell>
      </div>
    </van-cell-group>

    <a-drawer
      v-model:visible="visible"
      class="custom-class"
      placement="right"
      maskStyle="background-color: rgb(0 0 0 / 10%);"
      @after-visible-change="afterVisibleChange"
      getContainer=""
    >
      <template #title> {{ drawerInfo.name }}</template>

      <a-descriptions
        bordered
        size="middle"
        :column="{ xxl: 4, xl: 4, lg: 3, md: 3, sm: 2, xs: 1 }"
      >
        <template #title> {{ drawerInfo.name }}</template>
        <a-descriptions-item span="4">
          <template #label>
            <span class="drscriptionLabel">職缺名稱</span>
          </template>
          {{ drawerInfo.name }}
        </a-descriptions-item>

        <a-descriptions-item span="2">
          <template #label>
            <span class="drscriptionLabel">公司名稱</span>
          </template>
          {{ drawerInfo.company_name }}
        </a-descriptions-item>

        <a-descriptions-item span="1">
          <template #label>
            <span class="drscriptionLabel">上班地點</span>
          </template>
          {{ drawerInfo.name }}
        </a-descriptions-item>

        <a-descriptions-item label="上班地點"
          >{{ drawerInfo.area }}{{ drawerInfo.address }}
        </a-descriptions-item>

        <a-descriptions-item label="職務類別">
          <template v-for="(x, index) in drawerInfo.category"
            >{{ x }}
            <template v-if="index != drawerInfo.category.length - 1"
              >、
            </template>
          </template>
        </a-descriptions-item>
        <a-descriptions-item label="需求人數">{{
          drawerInfo.needEmployee
        }}</a-descriptions-item>
      </a-descriptions>

      <a-descriptions layout="vertical" bordered>
        <a-descriptions-item label="工作內容">
          {{ drawerInfo.jobDesc }}
        </a-descriptions-item>
      </a-descriptions>

      <a-descriptions
        bordered
        size="middle"
        :column="{ xxl: 4, xl: 4, lg: 3, md: 3, sm: 2, xs: 1 }"
      >
        <a-descriptions-item span="4">
          <template #label>
            <span class="drscriptionLabel">出差外派</span>
          </template>
          {{ drawerInfo.businessTrip }}
        </a-descriptions-item>

        <a-descriptions-item span="4">
          <template #label>
            <span class="drscriptionLabel">上班時段</span>
          </template>
          {{ drawerInfo.workPeriod }}
        </a-descriptions-item>

        <a-descriptions-item span="4">
          <template #label>
            <span class="drscriptionLabel">管理責任</span>
          </template>
          {{ drawerInfo.manageRespon }}
        </a-descriptions-item>

        <a-descriptions-item>
          <template #label>
            <span class="drscriptionLabel">條件要求</span>
          </template>
          <template v-for="(x, index) in drawerInfo.roleDesc"
            >{{ x }}
            <template v-if="index != drawerInfo.roleDesc.length - 1"
              >、
            </template>
          </template>
        </a-descriptions-item>

        <a-descriptions-item>
          <template #label>
            <span class="drscriptionLabel">可上班日</span>
          </template>
          {{ drawerInfo.startWorkDay }}
        </a-descriptions-item>

        <a-descriptions-item>
          <template #label>
            <span class="drscriptionLabel">學歷要求</span>
          </template>
          {{ drawerInfo.edu }}
        </a-descriptions-item>

        <a-descriptions-item>
          <template #label>
            <span class="drscriptionLabel">工作技能</span>
          </template>
          <template v-for="(x, index) in drawerInfo.skill"
            >{{ x }}
            <template v-if="index != drawerInfo.skill.length - 1">、 </template>
          </template>
        </a-descriptions-item>

        <a-descriptions-item>
          <template #label>
            <span class="drscriptionLabel">具備駕照</span>
          </template>
          <template v-for="(x, index) in drawerInfo.driverLicense"
            >{{ x }}
            <template v-if="index != drawerInfo.driverLicense.length - 1"
              >、
            </template>
          </template>
        </a-descriptions-item>
      </a-descriptions>

      <div class="van-safe-area-bottom" style="height: 60px"></div>
    </a-drawer>
  </div>

  <navBar />
</template>

<script>
// @ is an alias to /src
import navBar from "@/components/Navigation/NavBar";
import TopBarClickLeft from "@/components/Navigation/TopBarClickLeft";
import axios from "axios";
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
export default {
  name: "CompanyDetail",
  components: { navBar, TopBarClickLeft },

  setup() {
    const isShow = ref(true);
    const company = ref(null);
    const route = useRoute();

    const getData = async () => {
      let url = `/api/company/${route.params.id}`;
      await axios.get(url).then((response) => (company.value = response.data));
    };

    const extendText = () => {
      let text = document.getElementsByClassName("van-multi-ellipsis--l2");
      text[0].classList.remove("van-multi-ellipsis--l2");
      isShow.value = !isShow.value;
    };

    const visible = ref(false);
    const drawerInfo = ref("");

    const showDrawer = (job) => {
      drawerInfo.value = job;
      visible.value = true;
    };

    onMounted(() => {
      getData();
    });
    return {
      isShow,
      company,
      extendText,
      visible,
      drawerInfo,
      showDrawer,
    };
  },
};
</script>

<style>
.text-block {
  white-space: pre-line;
}

.home {
  padding-bottom: 0px;
}
.main-notice {
  padding: 20px;
}
.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
}
</style>

<template>
  <topBar />

  <div v-if="job !== null">
    <van-cell-group title="職缺" inset>
      <van-cell>
        <template #value
          ><h3>{{ job.name }}</h3>
        </template>
      </van-cell>
      <van-cell>
        <template #value
          ><h3>{{ job.company_name }}</h3>
        </template>
      </van-cell>
      <van-cell>
        <template #value>上班地點：{{ job.area }}{{ job.address }} </template>
      </van-cell>
      <van-cell>
        <template #value
          >職務類別：
          <template v-for="(x, index) in job.category"
            >{{ x }}
            <template v-if="index != job.category.length - 1">、 </template>
          </template>
        </template>
      </van-cell>
      <van-cell>
        <template #value>需求人數：{{ job.needEmployee }} </template>
      </van-cell>
      <van-cell>
        <template #value>更新日期：{{ job.jobUpDate }}</template>
      </van-cell>
    </van-cell-group>

    <van-cell-group title="工作內容">
      <van-cell>
        <template #value>
          <div class="text-block van-multi-ellipsis--l2">
            {{ job.jobDesc }}
          </div>
          <van-button type="default" @click="extendText()" v-show="isShow" block
            >更多
          </van-button>
        </template>
      </van-cell>
    </van-cell-group>

    <van-cell-group title="工作型態"
      ><van-cell>
        <template #value>出差外派：{{ job.businessTrip }} </template>
      </van-cell>
      <van-cell>
        <template #value>上班時段：{{ job.workPeriod }} </template>
      </van-cell>
      <van-cell>
        <template #value>休假制度：{{ job.vacationPolicy }} </template>
      </van-cell>
      <van-cell>
        <template #value>管理責任：{{ job.manageRespon }} </template>
      </van-cell>
    </van-cell-group>

    <van-cell-group title="條件要求">
      <van-cell>
        <template #value
          >接受身份：<template v-for="(x, index) in job.roleDesc"
            >{{ x }}
            <template v-if="index != job.roleDesc.length - 1">、</template>
          </template></template
        >
      </van-cell>
      <van-cell>
        <template #value>可上班日：{{ job.startWorkDay }} </template>
      </van-cell>
      <van-cell>
        <template #value>學歷要求：{{ job.edu }} </template>
      </van-cell>
      <van-cell>
        <template #value
          >工作技能：<template v-for="(x, index) in job.skill"
            >{{ x }}
            <template v-if="index != job.skill.length - 1">、 </template>
          </template></template
        >
      </van-cell>
      <van-cell>
        <template #value
          >具備駕照：<template v-for="(x, index) in job.driverLicense"
            >{{ x }}
            <template v-if="index != job.driverLicense.length - 1"
              >、
            </template></template
          ></template
        >
      </van-cell>
    </van-cell-group>

    <!-- <van-cell-group title="聯絡方式">
      <van-cell>
        <template #value>聯絡人：{{ job.jobCompany.contactPerson }} </template>
      </van-cell> -->
    <!-- <van-cell>
        <template #value>Email：{{ job.startWorkDay }} </template>
      </van-cell> -->
    <!-- </van-cell-group> -->
  </div>

  <navBar />
</template>

<script>
// @ is an alias to /src
import navBar from "@/components/Navigation/NavBar";
import topBar from "@/components/Navigation/TopBarClickLeft";
import axios from "axios";
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
export default {
  name: "JobDetail",
  components: { navBar, topBar },
  setup() {
    const isShow = ref(true);
    const job = ref(null);
    const route = useRoute();

    const extendText = () => {
      let text = document.getElementsByClassName("van-multi-ellipsis--l2");
      text[0].classList.remove("van-multi-ellipsis--l2");
      isShow.value = !isShow.value;
    };

    onMounted(async () => {
      let url = `/api/job/${route.params.id}`;
      await axios.get(url).then((response) => {
        job.value = response.data;
      });
    });

    return { isShow, job, extendText };
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

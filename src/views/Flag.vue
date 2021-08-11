<!--
 * @Author: flwfdd
 * @Date: 2021-08-11 14:53:47
 * @LastEditTime: 2021-08-11 22:50:50
 * @Description: 
 * _(:з」∠)_
-->
<template>
  <v-container fluid>
    <v-btn
      fab
      bottom
      right
      fixed
      color="green"
      dark
      @click="dialog_input = true"
      ><v-icon>add</v-icon></v-btn
    >

    <v-row class="mx-1 mt-1">
      <v-alert color="cyan" text>flw拥有<br />{{ wallet.flw }}瓶酸奶</v-alert>
      <v-spacer></v-spacer>
      <p class="text-center blue-grey--text ma-0" style="font-size: 4.2rem">
        约定
      </p>
      <v-spacer></v-spacer>
      <v-alert color="orange" text>xy拥有<br />{{ wallet.xy }}瓶酸奶</v-alert>
    </v-row>

    <v-tabs grow color="cyan" v-model="tab">
      <v-tab class="cyan--text">进行中</v-tab>
      <v-tab class="green--text">已完成</v-tab>
      <v-tab class="red--text">未完成</v-tab>
    </v-tabs>

    <v-tabs-items v-model="tab">
      <v-tab-item>
        <v-card>
          <v-list nav>
            <v-list-item-group color="cyan">
              <v-list-item
                two-line
                v-for="i in list.going"
                :key="i.id"
                @click="
                  i.status = true;
                  update_data = i;
                  dialog_update = true;
                "
              >
                <v-list-item-content>
                  <v-list-item-title>{{ i.name }}</v-list-item-title>
                  <v-list-item-subtitle>
                    {{ i.user }} | 到期:{{ i.due_date }} | 赌注:{{ i.value }} |
                    创建：{{ i.start_date }}
                  </v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </v-card>
      </v-tab-item>

      <v-tab-item>
        <v-card>
          <v-list nav>
            <v-list-item-group color="green">
              <v-list-item two-line v-for="i in list.success" :key="i.id">
                <v-list-item-content>
                  <v-list-item-title>{{ i.name }}</v-list-item-title>
                  <v-list-item-subtitle>
                    {{ i.user }} | 完成:{{ i.end_date }}| 到期:{{
                      i.due_date
                    }}
                    | 赌注:{{ i.value }} | 创建：{{ i.start_date }}
                  </v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </v-card>
      </v-tab-item>

      <v-tab-item>
        <v-card>
          <v-list nav>
            <v-list-item-group color="red">
              <v-list-item two-line v-for="i in list.fail" :key="i.id">
                <v-list-item-content>
                  <v-list-item-title>{{ i.name }}</v-list-item-title>
                  <v-list-item-subtitle>
                    {{ i.user }} | 完成:{{ i.end_date }} | 到期:{{
                      i.due_date
                    }}
                    | 赌注:{{ i.value }} | 创建：{{ i.start_date }}
                  </v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
          </v-list>
        </v-card>
      </v-tab-item>
    </v-tabs-items>

    <v-dialog v-model="dialog_input" max-width="424px">
      <v-card>
        <v-card-title class="green lighten-4"> 添加约定 </v-card-title>

        <v-card-text>
          <v-text-field
            color="cyan"
            label="事件"
            v-model="input_data.name"
          ></v-text-field>
          <v-text-field
            color="cyan"
            label="赌注"
            type="number"
            v-model="input_data.value"
            suffix="瓶酸奶"
          ></v-text-field>
          <v-switch
            color="cyan"
            class="ma-0"
            v-model="input_data.switch"
            :label="'一起吗？' + (input_data.switch ? '是' : '否')"
          ></v-switch>
          <v-date-picker
            elevation="24"
            full-width
            color="cyan"
            v-model="input_data.due_date"
            title="开始时间"
          ></v-date-picker>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red" text @click="dialog_input = false">关闭</v-btn>
          <v-btn color="green" text @click="Submit">提交</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="dialog_update" max-width="424px">
      <v-card>
        <v-card-title class="cyan lighten-4"> 更新约定 </v-card-title>

        <v-card-text>
          <v-switch
            color="green"
            v-model="update_data.status"
            :label="update_data.status ? '成功' : '失败'"
          ></v-switch>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red" text @click="dialog_update = false">关闭</v-btn>
          <v-btn color="green" text @click="Update">提交</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-snackbar v-model="snackbar" color="blue">
      {{ snackbar_msg }}
      <template v-slot:action="{ attrs }">
        <v-btn color="white" text v-bind="attrs" @click="snackbar = false"
          >Close</v-btn
        >
      </template>
    </v-snackbar>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    dialog_input: false,
    input_data: {
      name: "",
      due_date: "",
      value: 0,
      switch: false,
    },
    snackbar: false,
    snackbar_msg: "",
    list: {
      going: [],
      success: [],
      fail: [],
    },
    tab: 0,
    dialog_update: false,
    update_data: {},
    wallet: {
      xy: 0,
      flw: 0,
    },
  }),
  methods: {
    Submit() {
      this.$axios
        .get(this.$axios.defaults.api + "/save_flag/", {
          params: {
            user: this.input_data.switch ? "together" : this.GetCookie().user,
            name: this.input_data.name,
            start_date: this.FormatDate(new Date()),
            due_date: this.input_data.due_date,
            status: -1,
            value: this.input_data.value,
          },
        })
        .then(() => {
          this.dialog_input = false;
          this.Msg("提交成功awa");
        })
        .catch((err) => {
          console.log(err);
          this.Msg("提交失败");
        });
    },
    Get() {
      this.$axios
        .get(this.$axios.defaults.api + "/get_flag_list/", {
          params: {},
        })
        .then((res) => {
          let list = res.data.list;
          for (let i in list) {
            if (list[i].status == -1) this.list.going.push(list[i]);
            else if (list[i].status == 1) this.list.success.push(list[i]);
            else this.list.fail.push(list[i]);
          }
          this.list.going = this.list.going.sort((a, b) =>
            a.due_date > b.due_date ? 1 : -1
          );
          this.list.success = this.list.success.sort((a, b) =>
            a.end_date > b.end_date ? 1 : -1
          );
          this.list.fail = this.list.fail.sort((a, b) =>
            a.end_date > b.end_date ? 1 : -1
          );
        })
        .catch((err) => {
          console.log(err);
        });
    },
    GetWallet() {
      this.$axios
        .get(this.$axios.defaults.api + "/get_wallet/", {
          params: {},
        })
        .then((res) => {
          for (let i in res.data.list) {
            this.wallet[res.data.list[i].user] = res.data.list[i].count;
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
    Update() {
      this.$axios
        .get(this.$axios.defaults.api + "/update_flag/", {
          params: {
            id: this.update_data.id,
            status: Number(this.update_data.status),
            end_date: this.FormatDate(new Date()),
          },
        })
        .then(() => {
          this.dialog_update = false;
          this.Msg("更新成功awa");
        })
        .catch((err) => {
          console.log(err);
          this.Msg("更新失败Orz");
        });
    },
    FormatDate(date) {
      return (
        date.getFullYear() +
        "-" +
        (date.getMonth() + 1).toString().padStart(2, "0") +
        "-" +
        date.getDate()
      );
    },
    GetCookie() {
      let l = document.cookie.split(";");
      let dic = {};
      for (let i of l) {
        let ll = i.split("=");
        dic[ll[0]] = ll[1];
      }
      return dic;
    },
    Msg(msg) {
      this.snackbar_msg = msg;
      this.snackbar = true;
    },
  },
  created() {
    window.vm = this;
    this.Get();
    this.GetWallet();
  },
};
</script>
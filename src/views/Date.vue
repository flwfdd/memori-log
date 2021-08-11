<!--
 * @Author: flwfdd
 * @Date: 2021-08-11 00:51:09
 * @LastEditTime: 2021-08-11 17:59:46
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
    <p class="text-center blue-grey--text ma-n4" style="font-size: 4.2rem">
      记念
    </p>
    <v-card>
      <v-card-text>
        <v-row>
          <v-btn outlined icon @click="MoveMonth(-1)"
            ><v-icon>keyboard_arrow_left</v-icon></v-btn
          >
          <v-spacer></v-spacer>
          <p style="font-size: 1.24rem">{{ active_date.substring(0, 4) }}</p>
          <v-spacer></v-spacer>
          <v-btn outlined icon @click="MoveMonth(1)"
            ><v-icon>keyboard_arrow_right</v-icon></v-btn
          >
        </v-row>
        <v-calendar
          ref="calendar"
          @click:event="ShowEvent"
          :value="active_date"
          :events="events"
        ></v-calendar>
      </v-card-text>
    </v-card>

    <v-dialog v-model="dialog_event" max-width="424px">
      <v-card>
        <v-card-title :class="dialog_data.color + ' white--text'">
          记念
        </v-card-title>

        <v-card-title>
          {{ dialog_data.start }}
        </v-card-title>
        <v-card-title>
          {{ dialog_data.user }}
          {{ dialog_data.name }}
        </v-card-title>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="red" text @click="dialog_event = false">关闭</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="dialog_input" max-width="424px">
      <v-card>
        <v-card-title class="green lighten-4"> 添加记念 </v-card-title>

        <v-card-text justify="center">
          <v-text-field
            color="cyan"
            label="事件"
            v-model="input_data.name"
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
            v-model="input_data.date"
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
    active_date: "2004-02-04",
    events: [],
    dialog_event: false,
    dialog_data: {},
    input_data: {
      date: "",
      name: "",
      user: "",
      switch: false,
    },
    color_table: {
      flw: "cyan",
      xy: "orange",
      together: "pink lighten-2",
    },
    dialog_input: false,
    snackbar: false,
    snackbar_msg: "",
  }),
  methods: {
    MoveMonth(x) {
      let date = new Date(
        new Date(this.active_date).getTime() + x * 31 * 24 * 3600 * 1000
      );
      this.active_date =
        date.getFullYear() +
        "-" +
        (date.getMonth() + 1).toString().padStart(2, "0") +
        "-15";
    },
    ShowEvent({ event }) {
      this.dialog_data = event;
      this.dialog_event = true;
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
    Submit() {
      this.$axios
        .get(this.$axios.defaults.api + "/save_date/", {
          params: {
            user: this.input_data.switch ? "together" : this.GetCookie().user,
            name: this.input_data.name,
            date: this.input_data.date,
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
        .get(this.$axios.defaults.api + "/get_date_list/", {
          params: {
            start_date: this.FormatDate(
              new Date(
                new Date(this.active_date).getTime() - 42 * 24 * 3600 * 1000
              )
            ),
            end_date: this.FormatDate(
              new Date(
                new Date(this.active_date).getTime() + 42 * 24 * 3600 * 1000
              )
            ),
          },
        })
        .then((res) => {
          this.events = [];
          for (let i in res.data.list) {
            this.events.push({
              start: res.data.list[i].date,
              user: res.data.list[i].user,
              color: this.color_table[res.data.list[i].user],
              name: res.data.list[i].name,
            });
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
    Msg(msg) {
      this.snackbar_msg = msg;
      this.snackbar = true;
    },
  },
  watch: {
    active_date() {
      this.Get();
    },
  },
  created() {
    this.dialog_data.date = this.active_date = this.FormatDate(new Date());
  },
};
</script>
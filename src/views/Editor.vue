<!--
 * @Author: flwfdd
 * @Date: 2021-08-05 23:25:35
 * @LastEditTime: 2021-08-11 00:30:30
 * @Description: 
 * _(:з」∠)_
-->
<template>
  <v-container>
    <v-card class="my-3">
      <v-card-text>
        <v-text-field
          color="cyan"
          label="标题"
          v-model="doc.title"
        ></v-text-field>
        <v-text-field
          color="cyan"
          label="标签"
          v-model="doc.tag"
        ></v-text-field>
        {{ doc.user }} | {{ doc.tag }} | {{ doc.id }}
        <br />
        创建:{{ FormatDate(doc.first_time) }} | 更改:{{
          FormatDate(doc.last_time)
        }}
        <br />
        <v-btn block outlined color="green" @click="Preview" class="mb-2"
          >预览</v-btn
        >
        <v-btn block outlined color="cyan" @click="Save">保存</v-btn>
      </v-card-text>
    </v-card>

    <v-card id="editorjs" class="pa-3 blue-grey--text text--darken-2"></v-card>

    <br />
    <v-card>
      <v-card-text>
        <v-btn block outlined color="green" @click="Preview" class="mb-2"
          >预览</v-btn
        >
        <v-btn block outlined color="cyan" @click="Save">保存</v-btn>
      </v-card-text>
    </v-card>

    <v-snackbar v-model="snackbar" color="blue">
      {{ snackbar_msg }}
      <template v-slot:action="{ attrs }">
        <v-btn color="white" text v-bind="attrs" @click="snackbar = false"
          >Close</v-btn
        >
      </template>
    </v-snackbar>

    <v-dialog v-model="dialog" fullscreen transition="dialog-bottom-transition">
      <v-toolbar dense color="cyan white--text">
        <v-toolbar-title>预览</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn icon dark @click="dialog = false">
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </v-toolbar>
      <m-render :data="doc"></m-render>
    </v-dialog>
  </v-container>
</template>

<script>
import EditorJS from "@editorjs/editorjs";
const Quote = require("@editorjs/quote");
import ImageTool from "@editorjs/image";
import MRender from "../components/Render/MRender.vue";

export default {
  components: {
    MRender,
  },
  data: () => ({
    editor: "",
    doc: {
      id: -1,
      title: "",
      user: "",
      tag: "记",
      first_time: 0,
      last_time: 0,
      blocks: [],
    },
    snackbar: false,
    snackbar_msg: "",
    dialog: false,
  }),
  methods: {
    Save() {
      this.editor
        .save()
        .then((outputData) => {
          //console.log("Article data: ", outputData);
          this.doc.last_time = Math.round(new Date().getTime() / 1000);
          this.doc.blocks = outputData.blocks;
          this.$axios
            .post(this.$axios.defaults.api + "/save_doc/", this.doc)
            .then((res) => {
              //console.log(res);
              this.doc.id = res.data.id;
              this.Msg("保存成功awa");
            })
            .catch((err) => {
              console.log(err);
              this.Msg("保存失败orz");
            });
        })
        .catch((err) => {
          console.log("Save failed: ", err);
          this.Msg("保存失败orz");
        });
    },
    Preview() {
      this.editor
        .save()
        .then((outputData) => {
          //console.log("Article data: ", outputData);
          this.doc.last_time = Math.round(new Date().getTime() / 1000);
          this.doc.blocks = outputData.blocks;
          this.dialog = true;
        })
        .catch((err) => {
          console.log("Save failed: ", err);
          this.Msg("预览失败Orz");
        });
    },
    Get() {
      this.$axios
        .get(this.$axios.defaults.api + "/get_doc/?id=" + this.doc.id)
        .then((res) => {
          this.doc = res.data;
          this.doc.blocks = JSON.parse(this.doc.blocks);
          this.editor.render(this.doc);
          this.Msg("加载成功awa");
        })
        .catch((err) => {
          console.log("Get failed: ", err);
          this.Msg("加载失败orz");
        });
    },
    FormatDate(t) {
      var now = new Date(t * 1000);
      var year = now.getFullYear();
      var month = now.getMonth() + 1;
      var date = now.getDate();
      var hour = now.getHours();
      var minute = now.getMinutes();
      var second = now.getSeconds();
      return (
        year +
        "-" +
        month.toString().padStart(2,'0') +
        "-" +
        date.toString().padStart(2,'0') +
        " " +
        hour.toString().padStart(2,'0') +
        ":" +
        minute.toString().padStart(2,'0') +
        ":" +
        second.toString().padStart(2,'0')
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
    //初始化编辑器
    this.editor = new EditorJS({
      holder: "editorjs",
      tools: {
        quote: Quote,
        image: {
          class: ImageTool,
          config: {
            endpoints: {
              byFile: this.$axios.defaults.api + "/upload_img/", // Your backend file uploader endpoint
              byUrl: "",
            },
          },
        },
      },
    });

    this.editor.isReady.then(() => {
      //初始化文章
      if (this.$route.query.id) {
        this.doc.id = this.$route.query.id;
        this.Get();
      } else {
        //新建文章
        this.doc.user = this.GetCookie()["user"];
        let now = new Date();
        this.doc.last_time = this.doc.first_time = Math.round(
          now.getTime() / 1000
        );
        this.doc.title =
          "【" +
          now.getFullYear().toString() +
          (now.getMonth() + 1).toString().padStart(2, "0") +
          now.getDate().toString().padStart(2, "0") +
          "】";
      }
    });
  },
};
</script>
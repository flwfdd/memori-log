<!--
 * @Author: flwfdd
 * @Date: 2021-07-15 10:56:23
 * @LastEditTime: 2021-08-11 15:26:00
 * @Description: 
 * _(:з」∠)_
-->
<template>
  <div id="app">
    <v-app>
      <v-navigation-drawer app v-model="drawer">
        <v-list-item>
          <v-list-item-avatar>
            <img alt="Vue logo" src="./assets/memori.png" />
          </v-list-item-avatar>
          <v-list-item-title>memori</v-list-item-title>
          <v-spacer></v-spacer>
        </v-list-item>

        <v-divider></v-divider>

        <v-list dense nav>
          <v-list-item-group color="cyan">
            <v-list-item
              v-for="item in items"
              :key="item.title"
              @click="Go(item.link)"
            >
              <v-list-item-icon>
                <v-icon>{{ item.icon }}</v-icon>
              </v-list-item-icon>

              <v-list-item-content>
                <v-list-item-title>{{ item.title }}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-item-group>
        </v-list>
      </v-navigation-drawer>

      <v-app-bar app color="pink accent-1">
        <v-app-bar-nav-icon
          color="white"
          @click="drawer = !drawer"
        ></v-app-bar-nav-icon>
        <v-app-bar-title class="white--text">memori</v-app-bar-title>
      </v-app-bar>

      <v-main>
        <router-view></router-view>
      </v-main>

      <v-footer app>
        <!-- -->
      </v-footer>
    </v-app>
  </div>
</template>

<script>
export default {
  data: () => ({
    drawer: false,
    items: [
      { title: "主页", icon: "home", link: "/" },
      { title: "登陆", icon: "fingerprint", link: "/Login" },
      { title: "记忆", icon: "library_books", link: "/Diary" },
      { title: "记念", icon: "date_range", link: "/Date" },
      { title: "约定", icon: "flag", link: "/Flag" },
    ],
  }),
  methods: {
    Go(url) {
      this.$router.push(url);
    },
  },
};
</script>


<style lang="scss">
#app {
  font-family: Noto Serif SC;
  font-style: normal;
  font-weight: 500;
}
</style>
<template>
	<div id="app">
		<NavigationBar />
		<router-view></router-view>
	</div>
</template>

<script>
import NavigationBar from './components/NavigationBar.vue'
require("./js/fontawesome")

export default {
	name: 'App',
	components: {
		NavigationBar,
	}
}
</script>

<style scoped>
#app {
	/* height: 100vh; */
	font-family: "Hiragino Kaku Gothic Pro", "ヒラギノ角ゴ Pro W3", メイリオ, Meiryo, "ＭＳ Ｐゴシック", "Helvetica Neue", Helvetica, Arial, sans-serif;
}
button.transparent {
    margin: 5px;
    background: transparent;
    border: none;
  }
input.transparent {
    width: 100%;
    border: none;
  }
input.transparent:focus {
    outline: none;
    -webkit-box-shadow: none;
    box-shadow: none;
  }
</style>
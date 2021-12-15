<template>
	<div id="app">
		<NavigationBar />
		<MainPage />
	</div>
</template>

<script>
import NavigationBar from './components/NavigationBar.vue'
import MainPage from './components/MainPage.vue'
require("./js/fontawesome")

export default {
	name: 'App',
	components: {
		NavigationBar,
		MainPage,
	}
}
</script>

<style scoped>
#app {
	/* height: 100vh; */
	font-family: "Hiragino Kaku Gothic Pro", "ヒラギノ角ゴ Pro W3", メイリオ, Meiryo, "ＭＳ Ｐゴシック", "Helvetica Neue", Helvetica, Arial, sans-serif;
}
</style>
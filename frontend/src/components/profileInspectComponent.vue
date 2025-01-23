<template>
	<div class="profile_inspect_container">
		<div class="profile_inspect_name">
			profile of player {{profile.name}}
		</div>
		<div class="photo_container">
			<img v-if="profile.photo" :src="profile.photo" alt="profile picture of the player">
			<img v-else src="../../../static/photos/question_mark.jpg" alt="bit question mark becouse of no profile picture">
		</div>
		<div class="profile_inspect_border">
			<div class="profile_inspect_data_container">
				<div class="profile_inspect_box1">
					<div class="data_box">Poziom:</div>
					<div class="data_box">Rasa:</div>
					<div class="data_box">Ranking:</div>
				</div>
				<div class="profile_inspect_box2">
					<div class="data_box font_for_data">{{profile.lvl}} lvl</div>
					<div class="data_box font_for_data">{{profile.race}}</div>
					<div class="data_box font_for_data">{{profile.ranking_place}}</div>
				</div>

			</div>
		</div>

	</div>
</template>

<script>

export default {
	name: 'ProfileInspectComponent',
	props: ['profile'],
	components: {
		
	},
};
</script>

<style scoped>
img {
	object-fit: cover;
    width: 100%;
    height: 100%;
}

.profile_inspect_container {
	display: flex;
	justify-content: center;
	align-items: center;
	flex-direction: column;

}
.profile_inspect_border{
	margin: 10px 0 10px 0;
	background-color: rgb(238, 238, 238);
	width: 400px;
	display: flex;
	justify-content: center;
	align-items: center;
	padding: 10px;
}

.profile_inspect_data_container {
	padding: 20px;
	border: 2px solid rgba(0, 0, 0, 0.304);
	border-radius: 10px;
	display: flex;
	justify-content: center;
	align-items: center;
	width: 400px;

}

.profile_inspect_name {
	font-size: 20px;
	font-weight: bold;
	margin-bottom: 20px;
}

.photo_container {
	width: 400px;
}

.profile_inspect_box1, .profile_inspect_box2 {
	width: 40%;
}


.data_box {
	/* margin: 0 10px 0 10px; */
	width: 100%;
	display: flex;
	justify-content: flex-start;
	align-items: flex-start;
    font-size: 12px;
}

.name {
    font-size: 16px;
	justify-self: center;
}

.font_for_data {
	font-weight: bold;
	font-size: 13px;
}

@media (max-width: 800px) {
	.photo_container {
		width: 60%;
	}
	.profile_inspect_border{
		width: 60%;
	}
}
</style>

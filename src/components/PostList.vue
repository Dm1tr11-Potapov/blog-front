<template>
    <h2 style="text-align: center">Read another posts:</h2>
    <div class="post-list">
        <post-item 
        v-for="post in posts" :key="post.id" :post="post"/>
    </div>
</template>

<script>
import PostItem from './PostItem.vue';

export default {
    components:{
        PostItem,
    },
    props: {
        posts: Array,
    }
}
</script>
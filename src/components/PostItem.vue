<template>
    <div class="post-item">
        <h2>{{post.title}}</h2>
        <p>{{post.content}}</p>
        <comment
            v-for="comment in post.comments"
            :key="comment.id"
            :comment="comment"        
        ></comment>
    </div>
</template> 

<script>
import Comment from "./PostComment.vue";

export default {
    components:{
        Comment,
    },
    props: {
        post: Object
    }
}
</script>

<style scoped>
.post-item {
    margin: 20px;
    padding: 15px;
    border: 1px solid #d3d3d3;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0,0,0,.1);
}

.post-item h2 {
    font-size: 24px;
    color: #666666;
}

.post-item p {
    color: #333333;
    font-size: 16px;
}
</style>
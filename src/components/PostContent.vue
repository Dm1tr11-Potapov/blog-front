<template>
    <div class="post-content">     
        <div class="content">
            
            <section class="content article">
                <h2 style="text-align: center;">Post about Big Data</h2>
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Fugit consectetur distinctio dolor, cumque porro voluptatibus a quas qui velit incidunt culpa assumenda cupiditate. Alias asperiores ducimus incidunt perspiciatis, maxime sed!
                Amet hic nam aspernatur at cumque tempore tempora, voluptatem, sed nihil expedita ipsa laboriosam fuga officiis, maxime repellendus ratione culpa. Assumenda, iste odio quos ex autem perspiciatis cupiditate quaerat laboriosam!
                Ad reiciendis deserunt repudiandae quod sequi labore veniam, ipsam illo. Veritatis eligendi quibusdam libero, at mollitia pariatur sequi rem, obcaecati velit amet a sapiente vel sunt voluptatibus voluptates. Doloremque, quo!
                Repellendus nesciunt tempore harum voluptatem ex est. Voluptate consequatur temporibus impedit minus esse. Repudiandae excepturi earum minus ullam magnam asperiores, eaque quidem? Doloremque eaque eveniet in autem est ad ex?
                Perferendis hic natus, sapiente iusto dicta delectus veritatis, ea consequatur autem dolor a tempore repudiandae itaque, nemo consequuntur. Quod nulla reiciendis odio praesentium! Illum earum aspernatur est dolores magnam nisi!
            </section>
            
            <post-db/>
            <post-list :posts="posts"/>
            
        </div>
        
        <aside class="sidebar">
            <h3 style="text-align: center;">Bla-bla-bla</h3>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quam laborum dolorum porro sequi optio explicabo molestias, maiores quas ad cupiditate distinctio, perspiciatis magni nesciunt! Exercitationem omnis quasi dolor illum aliquam?
            Nam harum itaque placeat id doloribus repudiandae, nihil quas sapiente eaque non eligendi. Incidunt expedita doloribus voluptatum totam deserunt. Enim blanditiis a molestiae. Velit perspiciatis veritatis pariatur! Consequatur, accusamus iste? Lorem ipsum dolor sit amet consectetur adipisicing elit. Delectus maxime ea odio omnis, iste incidunt cumque cum eligendi ratione, et voluptates explicabo beatae perferendis architecto molestiae quibusdam quod consectetur reiciendis.
            Odit, aliquid neque harum nulla fuga ratione aperiam ad aspernatur cumque autem est quas ipsum et consequuntur ex magnam pariatur iste, odio quos magni ipsa? Commodi dolores nam reprehenderit animi?
            Nostrum minima quis tenetur earum ad cupiditate rerum consequatur illo amet pariatur magni quod dicta vero repellat vitae et, corporis iusto, deleniti aspernatur eius laborum impedit repudiandae officia? Explicabo, rerum!
            Ea, icabo vero pariatur, modi earum nesciunt? Adipisci autem deserunt, suscipit maiores libero modi a ipsam quas ullam dolores eius iste deleniti, molestias officia nemo?
        </aside>
        
    </div>  
</template>

<script>

import PostDb from './PostDb.vue';
import PostList from './PostList.vue';
import axios from 'axios';

export default {
    components:{
        PostList,
        PostDb,
    },
    props: {
        PostContent: Object},     
        data() {
            return {
                posts: [],                
        }
    },
    created() {
        this.fetchPosts();
    },
    methods: {
        async fetchPosts() {
            try {
                const response = await axios.get('/api/posts');
                this.posts = response.data;
            } catch (error) {
                console.log(error);
            }
        }
    }
}
    
</script>

<style scoped>

.post-content{
    display: grid;
    grid-template-areas: 
    'header header'
    'div_top_hypers div_top_hypers'
    'content sidebar'  
    'footer footer';
    gap: 10px;
    grid-template-columns: 1fr 300px ;
 
} 
.sidebar {    
    margin-right: 50px;
    margin-left: 25px;
    margin-top: 50px;    
    float: right;
    color:rgb(47,46,46);    
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    font-size: 16px;
    font-style: italic; 
    text-align: justify;     
}

.content {
    margin: 10px;
    margin-top: 25px;
    margin-left: 25px;
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    text-align: justify;
    font-size: 18px;
}
</style>



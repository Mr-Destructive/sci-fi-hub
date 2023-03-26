<script>
  import { onMount } from 'svelte';
    import { getCookie } from '../utils';


  const token = getCookie('token');

  async function fetchUserData(apiUrl, token, query) {
    const resp = await fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({ query })
    });

    const { data } = await resp.json();
    console.log(data)
    return data.chapter;
  }

let chapter;
let chapterId;
  onMount(async () => {
    if (token) {
      const apiUrl = 'http://localhost:8000/graphql/';
      const url = window.location.href;
      let segment = url.split('/');
      chapterId = segment[segment.length - 1];
      console.log(chapterId)
      const query = `query{chapter(chapterId:${chapterId}){id, name, textContent, order, book{author{username}}}}`;
      chapter = await fetchUserData(apiUrl, token, query);
      console.log(chapter);
    }
  });
</script>

{#if chapter}
<p>
  {chapter.name} - By <i>"{chapter.book.author.username}"</i>
  {chapter.textContent}
  {chapter.id}
</p>
{/if}

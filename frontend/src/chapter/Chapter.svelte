<script>
let bookId;
  import { onMount } from 'svelte';
  import { getCookie } from '../utils';
  import Edit from './Edit.svelte';
  import Delete from './Delete.svelte';


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
    return data.chapter;
  }

let chapter;
let chapterId;
  onMount(async () => {
    if (token) {
      const apiUrl = 'http://localhost:8000/graphql/';
      const url = window.location.href;
      let segment = url.split('/');
      bookId = segment[segment.length-3]
      chapterId = segment[segment.length - 1];
      const query = `
      query{
        chapter(
          bookId: ${bookId}, chapterId:${chapterId}
        ){
          id, name, textContent, order, book{author{username}}, status
        }
      }`;
      chapter = await fetchUserData(apiUrl, token, query);
    }
  });
  let render = true
</script>

{#if chapter }
  <h2>{chapter.name}</h2>
  <h3>- By <i>"{chapter.book.author.username}"</i></h3>
  <p>
      <Edit bind:render={render} bind:chapter bind:bookId/>
      <Delete bind:render={render} bind:chapter bind:bookId/>
  </p>
  <p>
      {chapter.textContent}
  </p>
{/if}

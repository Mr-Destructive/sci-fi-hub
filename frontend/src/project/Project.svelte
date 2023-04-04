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
    return data.project;
  }

let project;
let projectId;
  onMount(async () => {
    if (token) {
      const apiUrl = 'http://localhost:8000/graphql/';
      const url = window.location.href;
      let segment = url.split('/');
      projectId = segment[segment.length - 1];
      const query = `query{project(projectId:${projectId}){id, name, bookSet{name, id}}}`;
      project = await fetchUserData(apiUrl, token, query);
    }
  });
</script>

{#if project}
  <h2>
    {project.name}
  </h2>
  {#each project.bookSet as book}
      <li><a href="#/book/{book.id}">{book.name}</a></li>
  {/each}
{/if}

<script>
  import { onMount } from 'svelte';
  import { getCookie } from '../utils';

  const token = getCookie('token');

  async function fetchProjectData(apiUrl, token, query) {
    const resp = await fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({ query })
    });

    const { data } = await resp.json();
    return data.projects;
  }

  let projects = [];
  onMount(async () => {
    if (token) {
      const apiUrl = 'http://localhost:8000/graphql/';
      const query = 'query{projects{id, name}}';
      projects = await fetchProjectData(apiUrl, token, query);
    }
  });
</script>

<a href='#/add/projects/'><button>Add Project</button></a>
{#if projects }
    <ul>
    {#each projects as project}
        <li><a href="/#/project/{project.id}">{project.name}</a></li>
    {/each}
    </ul>
{:else}
  <p>Please Login to view your Projects</p>
{/if}

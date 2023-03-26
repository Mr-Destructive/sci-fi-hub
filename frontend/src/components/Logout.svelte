<script>
  import { deleteCookie } from "../utils.js"
  deleteCookie("refreshtoken");
  deleteCookie("token");
  window.location.href = '/';
</script>

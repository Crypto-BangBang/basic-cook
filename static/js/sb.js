/* Supabase client + helpers — used across all pages */
(function () {
  var client = supabase.createClient(
    'https://tinxnxdfgwbqodejiqge.supabase.co',
    'sb_publishable_KozFZVvyDFOOZfTJb8edJA_ziU1W6X3'
  );

  async function getUser() {
    var res = await client.auth.getSession();
    return res.data.session ? res.data.session.user : null;
  }

  window.SB = {
    client: client,
    getUser: getUser,

    async isFavorite(path) {
      var user = await getUser(); if (!user) return false;
      var res = await client.from('favorites').select('id').eq('user_id', user.id).eq('recipe_path', path).maybeSingle();
      return !!res.data;
    },

    async toggleFavorite(path) {
      var user = await getUser(); if (!user) return null;
      var res = await client.from('favorites').select('id').eq('user_id', user.id).eq('recipe_path', path).maybeSingle();
      if (res.data) {
        await client.from('favorites').delete().eq('id', res.data.id);
        return false;
      }
      await client.from('favorites').insert({ user_id: user.id, recipe_path: path });
      return true;
    },

    async getFavorites() {
      var user = await getUser(); if (!user) return null;
      var res = await client.from('favorites').select('recipe_path').eq('user_id', user.id);
      return (res.data || []).map(function (r) { return r.recipe_path; });
    },

    async getCookCount(path) {
      var user = await getUser(); if (!user) return null;
      var res = await client.from('cooking_logs').select('count').eq('user_id', user.id).eq('recipe_path', path).maybeSingle();
      return res.data ? res.data.count : 0;
    },

    async logCook(path) {
      var user = await getUser(); if (!user) return null;
      var res = await client.from('cooking_logs').select('id, count').eq('user_id', user.id).eq('recipe_path', path).maybeSingle();
      if (res.data) {
        var n = res.data.count + 1;
        await client.from('cooking_logs').update({ count: n, last_cooked: new Date().toISOString() }).eq('id', res.data.id);
        return n;
      }
      await client.from('cooking_logs').insert({ user_id: user.id, recipe_path: path, count: 1 });
      return 1;
    },

    async getNote(path) {
      var user = await getUser(); if (!user) return null;
      var res = await client.from('notes').select('content').eq('user_id', user.id).eq('recipe_path', path).maybeSingle();
      return res.data ? res.data.content : '';
    },

    async saveNote(path, content) {
      var user = await getUser(); if (!user) return;
      var res = await client.from('notes').select('id').eq('user_id', user.id).eq('recipe_path', path).maybeSingle();
      if (res.data) {
        await client.from('notes').update({ content: content, updated_at: new Date().toISOString() }).eq('id', res.data.id);
      } else {
        await client.from('notes').insert({ user_id: user.id, recipe_path: path, content: content });
      }
    },

    async getCourseProgress() {
      var user = await getUser(); if (!user) return null;
      var res = await client.from('course_progress').select('recipe_path').eq('user_id', user.id);
      return (res.data || []).map(function (r) { return r.recipe_path; });
    },

    async toggleProgress(path) {
      var user = await getUser(); if (!user) return null;
      var res = await client.from('course_progress').select('id').eq('user_id', user.id).eq('recipe_path', path).maybeSingle();
      if (res.data) {
        await client.from('course_progress').delete().eq('id', res.data.id);
        return false;
      }
      await client.from('course_progress').insert({ user_id: user.id, recipe_path: path });
      return true;
    },

    async signIn(email, password) {
      return client.auth.signInWithPassword({ email: email, password: password });
    },

    async signUp(email, password, username) {
      return client.auth.signUp({ email: email, password: password, options: { data: { username: username } } });
    },

    async signOut() { return client.auth.signOut(); },

    async updatePassword(newPw) { return client.auth.updateUser({ password: newPw }); },

    getUsername(user) {
      return (user.user_metadata && user.user_metadata.username) || user.email.split('@')[0];
    },
  };
})();

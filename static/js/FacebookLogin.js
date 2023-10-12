async function signInWithFacebook() {
    const { data, error } = await supabase.auth.signInWithOAuth({
      provider: 'facebook',
    })
  }

  async function signOut() {
    const { error } = await supabase.auth.signOut()
  }
  
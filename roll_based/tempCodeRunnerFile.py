user = User.query.filter_by(email=email, role=role).first()
    if user and check_password_hash(user.password, password):
        session['user_id'] = user.id
        session['role'] = user.role
        #flash('Login successful', 'success')
        if user.role == 'admin':
            return redirect(url_for('admin_home'))
        else:
            return redirect(url_for('user_home'))
    flash('Invalid credentials', 'danger')
    return redirect(url_for('index'))

@app.route('/admin_home')
def admin_home():
    if 'user_id' in session and session['role'] == 'admin':
        return render_template('admin_home.html')
    return redirect(url_for('index'))

@app.route('/user_home')
def user_home():
    if 'user_id' in session and session['role'] == 'user':
        return render_template('user_home.html')
    return redirect(url_for('index'))
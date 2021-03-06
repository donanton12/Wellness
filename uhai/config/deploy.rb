set :stages, %w(production staging)
set :default_stage, "staging"
set :stage_dir, "deploy"

#require 'capistrano/ext/multistage'

set :normalize_asset_timestamps, false

set :application, "uhai"
set :deploy_to, "~/webapp_releases/#{application}"
set :webapps_loc, "~/webapps/#{application}"
set :shared_children, %w(config lib upload database)

set :local_repository, ".git"
set :scm, :git

set :user, "uhai"
set :use_sudo, false

task :production do
    set :repository, "http://ian:n41l4b@git.synacor.co.ke/#{application}.git"
    set :python_command, "python"

    server "uhai-app.cloudapp.net", :app, :web, :primary => true
end

task :staging do
    set :repository, "~/webapps/git/repos/uhai.git"
    set :python_command, "PYTHONPATH=#{webapps_loc}/lib/python2.7:$PYTHONPATH python2.7"

    server "synacor.co.ke", :app, :web, :primary => true
end

namespace (:deploy) do
  task :restart do
    run "~/webapps/uhai/apache2/bin/restart"
  end

  task :finalize_update, :except => { :no_release => true } do
    django.static
    django.syncdb
  end
end

namespace (:django) do
  desc <<-DESC
    Run the "python manage.py collectstatic" task
  DESC
  task :static do
    run "mkdir -p #{latest_release}/static"
    run "cd #{latest_release} && #{python_command} manage.py collectstatic --noinput" 
  end
  
  desc <<-DESC
    Run the "python manage.py syncdb" task
  DESC
  task :syncdb do
    run "cd #{webapps_loc}/wellness && #{python_command} manage.py syncdb --noinput"
  end

  desc <<-DESC
    Run the "python manage.py reset web" task
  DESC
  task :reset do
    run "cd #{webapps_loc}/wellness && #{python_command} manage.py reset core records --noinput"
  end
end
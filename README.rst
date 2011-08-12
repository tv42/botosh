=================================================================
 Botosh -- start a Python interpreter with Boto connections open
=================================================================

To get started, type::

	./bootstrap

Set up your ``~/.botosh.yaml`` config file. The file format is YAML,
and it should contain a top-level ``s3`` section, with one or more
connections defined under it::

	s3:
	  aws:
	    aws_access_key_id: EDIT-ME
	    aws_secret_access_key: EDIT-ME

	  dho:
	    host: objects.dreamhost.com
	    access_key: EDIT-ME
	    secret_key: EDIT-ME

	  rgw:
	    host: localhost
	    port: 7280
	    is_secure: no
	    access_key: EDIT-ME
	    secret_key: EDIT-ME

Then you can run::

	./virtualenv/bin/botosh

to start an interactive Python session with the connections accessible
as ``s3.aws``, ``s3.dho``, ``s3.rgw`` -- whatever you defined in the
config file.

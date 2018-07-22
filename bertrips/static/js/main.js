/*
	Snapshot by TEMPLATED
	templated.co @templatedco
	Released for free under the Creative Commons Attribution 3.0 license (templated.co/license)
*/

(function($) {

	skel.breakpoints({
		xlarge: '(max-width: 1680px)',
		large: '(max-width: 1280px)',
		medium: '(max-width: 980px)',
		small: '(max-width: 736px)',
		xsmall: '(max-width: 480px)'
	});

	$(function() {

		var	$window = $(window),
			$body = $('body');

		// Disable animations/transitions until the page has loaded.
			$body.addClass('is-loading');

			$window.on('load', function() {
				window.setTimeout(function() {
					$body.removeClass('is-loading');
				}, 100);
			});

		// Fix: Placeholder polyfill.
			$('form').placeholder();

		// Prioritize "important" elements on medium.
			skel.on('+medium -medium', function() {
				$.prioritize(
					'.important\\28 medium\\29',
					skel.breakpoint('medium').active
				);
			});

		// Scrolly.
			$('.scrolly').scrolly();

		// Gallery.
			$('.gallery').each(function() {

				var	$gallery = $(this),
					$content = $gallery.find('.content');
					$img_center = $gallery.find('.img_center');

				// Poptrox.
					$img_center.poptrox({
						usePopupCaption: true
					});


				// Tabs.
					$gallery.each( function() {

						var $this = $(this),
							$tabs = $this.find('.tabs a'),
							$albumtab = $this.find('.albumtab'),
							$album = $this.find('.album'),
							$time = $this.find('.time'),
							$country = $this.find('.country'),
							$time_album = $this.find('.time_album'),
							$country_album = $this.find('.country_album'),
							$cat = $this.find('.cat');


						$tabs.on('click', function(e) {

							var $this = $(this),
								tag = $this.data('tag');

							// Prevent default.
							 	e.preventDefault();

							

							

							// Hide media that do not have the same class as the clicked tab.
								if(tag == "country_album")
								{
									// Remove active class from all tabs.
									$albumtab.removeClass('active');

									// Reapply active class to current tab.
									$this.addClass('active');

									$album
										.fadeOut('fast')
										.each(function() {

											var $this = $(this);

											if ($this.hasClass(tag))
												$this
													.fadeOut('fast')
													.delay(200)
													.queue(function(next) {
														$this.fadeIn();
														next();
													});

										});

									$country
										.fadeOut('fast')
										.each(function() {

											var $this = $(this);
											
											$this
												.fadeOut('fast')
												.delay(200)
												.queue(function(next) {
													$this.fadeIn();
													next();
												});

										});

									$country_album
										.fadeOut('fast')
										.each(function() {

											var $this = $(this),
											$tab = $this.find(".tabs a");

											$tab
												.each(function(){
													var $this = $(this);

													if(!$this.hasClass('active'))
														$this.addClass('active');
												})

											// $this
											// 	.fadeOut('fast')
											// 	.delay(200)
											// 	.queue(function(next) {
											// 		$this.fadeIn();
											// 		next();
											// 	});

										});
								}
								else if(tag == "time_album"){
									// Remove active class from all tabs.
									$albumtab.removeClass('active');

									// Reapply active class to current tab.
									$this.addClass('active');

									$album
										.fadeOut('fast')
										.each(function() {

											var $this = $(this);

											if ($this.hasClass(tag))
												$this
													.fadeOut('fast')
													.delay(200)
													.queue(function(next) {
														$this.fadeIn();
														next();
													});

										});

									$time
										.fadeOut('fast')
										.each(function() {

											var $this = $(this);
											
											$this
												.fadeOut('fast')
												.delay(200)
												.queue(function(next) {
													$this.fadeIn();
													next();
												});

										});

									$time_album
										.fadeOut('fast')
										.each(function() {

											var $this = $(this),
												$tab = $this.find(".tabs a");

												$tab
													.each(function(){
														var $this = $(this);

														if(!$this.hasClass('active'))
															$this.addClass('active');
													})

												// $this
												// 	.fadeOut('fast')
												// 	.delay(200)
												// 	.queue(function(next) {
												// 		$this.fadeIn();
												// 		next();
												// 	});

										});
								}
								else
								{	
									if ($this.hasClass('active'))
										$this.removeClass('active');
									else
										$this.addClass('active');	
									$cat
										.each(function() {

											// var $this = $(this);

											// if ($this.hasClass(tag))
											// 	$this
											// 		.fadeOut('fast')
											// 		.delay(200)
											// 		.queue(function(next) {
											// 			$this.fadeIn();
											// 			next();
											// 		});

											var $this = $(this);

											if($this.hasClass(tag))
											{
												if ($this.hasClass('activecat'))
												{
													$this
														.fadeOut('fast')
														.removeClass('activecat');
														// .delay(200)
														// .queue(function(next) {
														// 	$this.fadeIn();
														// 	next();
														// });.
												}
												else
												{
													$this
														.fadeOut('fast')
														.delay(200)
														.queue(function(next) {
															$this.fadeIn();
															next();
														})
														.addClass('activecat');
												}
											}

										});
								}

						});

					});


			});

	});

})(jQuery);
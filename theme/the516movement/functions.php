<?php
add_action('wp_enqueue_scripts', function(){ wp_enqueue_style('the516movement-fonts','https://fonts.googleapis.com/css2?family=Roboto+Condensed:wght@400;700&family=Inter:wght@400;600&display=swap',[],null); wp_enqueue_style('the516movement', get_stylesheet_uri(), [], wp_get_theme()->get('Version')); });
add_action('init', function(){ register_block_pattern_category('the516movement',['label'=>'The 516 Movement']); });

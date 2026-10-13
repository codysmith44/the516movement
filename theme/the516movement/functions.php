<?php
add_action('wp_enqueue_scripts', function(){ wp_enqueue_style('the516movement', get_stylesheet_uri(), [], wp_get_theme()->get('Version')); });
add_action('init', function(){ register_block_pattern_category('the516movement',['label'=>'The 516 Movement']); });

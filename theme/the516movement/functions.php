<?php
add_action('wp_enqueue_scripts', function(){
  $v = wp_get_theme()->get('Version');
  wp_enqueue_style('the516movement', get_stylesheet_uri(), [], $v);
  wp_enqueue_script('the516movement-reveal', get_theme_file_uri('assets/reveal.js'), [], $v, ['strategy'=>'defer','in_footer'=>true]);
});
add_action('wp_head', function(){ echo "<script>document.documentElement.classList.add('js');</script>\n"; }, 1);
add_action('init', function(){
  register_block_pattern_category('the516movement',['label'=>'The 516 Movement']);
  foreach (['light'=>'Light (glow)','ghost'=>'Ghost','text'=>'Text link'] as $k=>$l) register_block_style('core/button',['name'=>$k,'label'=>$l]);
});

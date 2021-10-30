import { Component, OnInit } from '@angular/core';
import { BlogPostService } from '../services/blog_post.service';

@Component({
  selector: 'app-blog-post',
  templateUrl: './blog-post.component.html',
  styleUrls: ['./blog-post.component.scss']
})
export class BlogPostComponent implements OnInit {

  constructor(
    private blogPostService: BlogPostService
  ) { }

  ngOnInit(): void {
      this.blogPostService.list().subscribe(response => {
        console.log(response);
      })  
  }
}
